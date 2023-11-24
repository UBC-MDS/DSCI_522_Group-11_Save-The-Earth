import pandas as pd
import pytest
import sys
import os
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.scoring_metrics import scoring_metrics

#Test Data
X,y = make_regression(n_samples=100,n_features=7,random_state=123)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=123)
model = KNeighborsRegressor()
model.fit(X_train,y_train)
# Test for correct return type
def test_scoring_metrics_returns_dataframe():
    result = scoring_metrics(model,X_train,y_train,X_test,y_test)
    assert isinstance(result, pd.DataFrame), "scoring_metrics` should return a pandas data frame"


# Test for non negative scores
def test_scoring_metric_non_negative():
    result = scoring_metrics(model,X_train,y_train,X_test,y_test)
    assert result['test_rmse'][0] >= 0
    assert result['test_r2'][0] >= 0
# Test for checking the metric columns
def test_scoring_metric_columns():
    result = scoring_metrics(model,X_train,y_train,X_test,y_test)
    print(result.columns)
    expected_columns = {'train_rmse', 'test_rmse', 'train_r2', 'test_r2'}
    assert set(result.keys()) == expected_columns

    
