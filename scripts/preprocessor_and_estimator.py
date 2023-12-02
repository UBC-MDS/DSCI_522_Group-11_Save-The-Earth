import click
import os
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import set_config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer, make_column_selector

from scipy.stats import randint
from sklearn.compose import make_column_transformer
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import make_scorer, mean_squared_error, r2_score
from sklearn.model_selection import RandomizedSearchCV, cross_validate
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVR

def data_preprocessor(drop_feats=None, passthrough_feats=None, categorical_feats=None, numerical_feats=None):
    """
    Create Sklearn Column Transformer to drop, passthrough, encode and scale specified features
    """
    steps = []
    if drop_feats is not None:
        steps.append(('drop', drop_feats))
    if passthrough_feats is not None:
        steps.append(('passthrough', passthrough_feats))
    if numerical_feats is not None:
        steps.append((StandardScaler(), numerical_feats))
    if categorical_feats is not None:
        steps.append((OneHotEncoder(handle_unknown='ignore', sparse_output=False, dtype='int'), categorical_feats))

    preprocessor = make_column_transformer(*steps)
    preprocessor.verbose_feature_names_out = False

    return preprocessor

@click.command()
@click.option('--training_data', type=str, help="Path to training data")
@click.option('--pipeline_to', type=str, help="Path to directory where the pipeline object will be written to")
@click.option('--results_to', type=str, help="Path to directory where the plot will be written to")
@click.option('--seed', type=int, help="Random seed", default=522)

def main (training_data, pipeline_to, results_to, seed):
    """
    Select and Train the preprocessor and estimator for co2 per capita prediction on the training data
    """
    np.random.seed(seed)

    # Load data
    train_df = pd.read_csv(training_data)
    X_train = train_df.drop(columns=["co2_e"])
    y_train = train_df["co2_e"]

    # Preprocessing
    # Lists of feature names
    drop_feats = ["year"]
    categorical_feats = ["country"]
    numerical_feats = [
        "coal_c",
        "elec_g",
        "elec_c",
        "hydro_g",
        "nuclear_g",
        "gas_g",
        "oil_c",
        "oil_g",
    ]

    # Create preprocessor
    preprocessor = data_preprocessor(
        drop_feats=drop_feats,
        categorical_feats=categorical_feats,
        numerical_feats=numerical_feats,
    )

    # Model Selection
    # List of models
    models = {
        "Baseline": DummyRegressor(),
        "KNN_reg": KNeighborsRegressor(),
        "Ridge": Ridge(),
        "SVR": SVR(),
    }
    # List of metrics
    score_types = {
        "r2": "r2",
    }

    # Evaluate models
    cross_val_results = dict()
    for name, model in models.items():
        pipe = make_pipeline(preprocessor, model)
        cross_val_results[name] = (
            pd.DataFrame(
                cross_validate(
                    pipe,
                    X_train,
                    y_train,
                    cv=10,
                    scoring=score_types,
                    return_train_score=True,
                )
            )
            .agg(["mean", "std"])
            .round(3)
            .T
        )

    cross_val_results_df = pd.concat(
        cross_val_results, axis="columns"
    )
    cross_val_results_df.to_csv(os.path.join(results_to, "model_selection_scores.csv"), index=True)
    cross_val_results_df.set_index(cross_val_results_df.columns[0], inplace=True)

    # Hyperparameter Optimization
    # List of hyperparameters
    param_dist = {
        "kneighborsregressor__n_neighbors": randint(1, 20),
        "columntransformer__onehotencoder__max_categories": randint(
            1, X_train["country"].unique().shape[0]
        ),
    }

    # Create Pipeline
    pipe_best_model = make_pipeline(
        preprocessor, KNeighborsRegressor()
    )

    # Random search on hyperparameters
    random_search = RandomizedSearchCV(
        pipe_best_model,
        param_distributions=param_dist,
        cv=10,
        n_iter=20,
        scoring=score_types,
        n_jobs=-1,
        refit="r2",
        return_train_score=True
    )
    random_search.fit(X_train, y_train)

    random_search_results_df = pd.DataFrame(random_search.cv_results_).sort_values('mean_test_r2', ascending=False)[
        [
            "param_columntransformer__onehotencoder__max_categories",
            "param_kneighborsregressor__n_neighbors",
            "mean_test_r2",
            "std_test_r2",
        ]
    ]
    random_search_results_df.to_csv(os.path.join(results_to, "hyperparameter_tuning_scores.csv"), index=False)

    best_estimator = random_search.best_estimator_
    with open(os.path.join(pipeline_to, "co2_pipeline.pickle"), 'wb') as f:
        pickle.dump(best_estimator, f)

    return

if __name__ == '__main__':
    main()
