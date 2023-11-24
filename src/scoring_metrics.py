import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error,r2_score

def scoring_metrics(model, X_train, y_train,X_test,y_test):
    """
    Calculate and return the performance metrics for a given regression model

    Parameters:
    ----------
    model : object
        The regression model
    X_train : DataFrame
        The features of training data
    y_train : DataFrame
        The target value/feature for the training data
    X_test : DataFrame
        The features for test data
    y_test : DataFrame
        The target value/feature for the test data

    Returns:
    -------
    pandas.DataFrame
        A dataframe containing 4 performance metric values:
        - train_rmse : It stores the RMSE value for trainig data
        - test_rmse : It stores the RMSE value for test data
        - train_r2 : It stores the R2 score for training data
        - test_r2 : It stores the R2 score for test data
        
    Examples:
    --------
    >>> from sklearn.neighbors import KNeighborsRegressor
    >>> model = KNeighborsRegressor()
    >>> metrics_df = scoring_metrics(model, X_train, y_train, X_test, y_test)
    >>> print(metrics_df)
    """
    train_rmse = np.sqrt(mean_squared_error(y_train, model.predict(X_train)))
    test_rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
    train_r2 = r2_score(y_train, model.predict(X_train))
    test_r2 = r2_score(y_test, model.predict(X_test))
    
    metrics = {
        'train_rmse' : train_rmse,
        'test_rmse' : test_rmse,
        'train_r2' : train_r2,
        'test_r2' : test_r2
    }

    result_metrics = pd.DataFrame(metrics,index=[0])

    return result_metrics
