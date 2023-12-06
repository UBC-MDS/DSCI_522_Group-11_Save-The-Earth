import click
import os
import numpy as np
import pandas as pd
import pickle
from scipy.stats import randint
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

@click.command()
@click.option('--train_data', type=str, help="Path to train data")
@click.option('--test_data', type=str, help="Path to test data")
@click.option('--columns_to_drop', type=str, help="Optional: columns to drop")
@click.option('--pipeline_from', type=str, help="Path to directory where the fit pipeline object lives")
@click.option('--results_to', type=str, help="Path to directory where the plot will be written to")
@click.option('--seed', type=int, help="Random seed", default=123)

def main(train_data,test_data, columns_to_drop, pipeline_from, results_to, seed):
    """Evaluates the co2 emission using regression on the test data 
    and saves the evaluation results.

    Parameters:
    -----------
    train_data : str
        The path of the training data csv file
    test_data : str
        The path of the test data csv file
    columns_to_drop : list, optional
        Give the list of columns to drop
    pipeline_from : str
        The path of the pipeline model
    results_to : str
        The path of directory where the results need to be stored
    seed : int
        The seed used for the evaluation, default is 123

    Returns:
    --------
    None

    Examples:
    ---------
    >>> $ python scripts/evaluate-save-on-earth.py \
            --train_data=Data/Processed/train_df.csv \
            --test_data=Data/Processed/test_df.csv \
            --pipeline_from=results/models/co2_pipeline.pickle \
            --results_to=results \
            --seed=123

    """
    np.random.seed(seed)
    # set_config(transform_output="pandas")

    # read in data & fit (pipeline object)
    saveonearth_train = pd.read_csv(train_data)
    saveonearth_test = pd.read_csv(test_data)
    if columns_to_drop:
        to_drop = pd.read_csv(columns_to_drop).feats_to_drop.tolist()
        saveonearth_train = saveonearth_train.drop(columns=to_drop)
        saveonearth_test = saveonearth_test.drop(columns=to_drop)
    with open(pipeline_from, 'rb') as f:
        saveonearth_fit = pickle.load(f)

    # Compute R2 score
    r2_score_train = r2_score(saveonearth_train["co2_e"], saveonearth_fit.predict(saveonearth_train.drop(columns=["co2_e"])))
    r2_score_test = r2_score(saveonearth_test["co2_e"], saveonearth_fit.predict(saveonearth_test.drop(columns=["co2_e"])))
    # Compute RMSE
    rmse_train =np.sqrt(mean_squared_error(saveonearth_train["co2_e"],
                                           saveonearth_fit.predict(saveonearth_train.drop(columns=["co2_e"]))))
    rmse_test = np.sqrt(mean_squared_error(saveonearth_test["co2_e"],
                                           saveonearth_fit.predict(saveonearth_test.drop(columns=["co2_e"]))))
    # Saving model scores and model predictions in a file
    model_scores = pd.DataFrame({'r2_score_train': [r2_score_train],'r2_score_test': [r2_score_test] ,'rmse_train': [rmse_train],'rmse_test': [rmse_test]})
    model_scores.to_csv(os.path.join(results_to, "tables/model_scores.csv"), index=False)

    model_predictions = pd.DataFrame({'actual': saveonearth_test["co2_e"],'predicted': saveonearth_fit.predict(saveonearth_test.drop(columns=["co2_e"])) })
    model_predictions.to_csv(os.path.join(results_to, "tables/model_predictions.csv"), index=False)
    #plotting the graphs
    plt.scatter(saveonearth_test["co2_e"], saveonearth_fit.predict(saveonearth_test.drop(columns=["co2_e"])), alpha=0.3)
    grid = np.linspace(saveonearth_test["co2_e"].min(), saveonearth_test["co2_e"].max(), 1000)
    plt.plot(grid, grid, "--k")
    plt.xlabel("actual values")
    plt.ylabel("predicted values")
    plt.title("Predicted Vs Actual values in Test data")
    fig = plt.gcf()
    ax = plt.gca()
    figure_path = os.path.join(results_to, "figures/scatter_plot.png")
    fig.savefig(figure_path)
    



if __name__ == '__main__':
    main()