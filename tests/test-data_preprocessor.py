# Initialize packages
import pandas as pd
import pytest
import sys
import os
from sklearn.compose import ColumnTransformer

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_preprocessor import data_preprocessor

# Test data
dataframe_1 = pd.DataFrame({
    "perf_score": [1.01, 2.15, 3.32, -1.58, 0.95, 0.95],
    "feedback": ["good", "bad", "good", "good", "average", "bad"],
    "id": ["a001", "a002", "a003", "a004", "a005", "a006"],
    "status": [1, 0, 1, 0, 0, 0]
})
drop_feat_1 = ['id']
passthrough_feat_1 = ['status']
numerical_feat_1 = ['perf_score']
categorical_feat_1 = ['feedback']
dataframe_1_list = [{
    "perf_score": [1.01, 2.15, 3.32, -1.58, 0.95, 0.95],
    "feedback": ["good", "bad", "good", "good", "average", "bad"],
    "id": ["a001", "a002", "a003", "a004", "a005", "a006"],
    "status": [1, 0, 1, 0, 0, 0]
}]
passthrough_feat_1_val = 'status'
numerical_feat_1_val = 'perf_score'
categorical_feat_1_val = 'feedback'
error_drop_feat_1 = ['id', 'id2']

# Expected outputs
encoded_dataframe_1 = pd.DataFrame({
    "status": [1., 0., 1., 0., 0., 0.],
    "perf_score": [1.01, 2.15, 3.32, -1.58, 0.95, 0.95],
    "feedback_average": [0., 0., 0., 0., 1., 0.],
    "feedback_bad": [0., 1., 0., 0., 0., 1.],
    "feedback_good": [1., 0., 1., 1., 0., 0.]
})

# Test for correct return type
def test_data_preprocessor_returns_columntransformer():
    result = data_preprocessor(drop_feat_1, passthrough_feat_1, categorical_feat_1, numerical_feat_1)
    assert isinstance(result, ColumnTransformer), "`data_preprocessor` should return a ColumnTransformer"

# Test for correct number of rows and columns in the transformed data
def test_data_preprocessor_dimensions():
    result = data_preprocessor(drop_feat_1, passthrough_feat_1, categorical_feat_1, numerical_feat_1)
    result_arr = result.fit_transform(dataframe_1)
    assert result_arr.shape[0] == encoded_dataframe_1.shape[0], "Transformed dataframe should have the same row as the original dataframe"
    assert result_arr.shape[1] == encoded_dataframe_1.shape[1], "Number of columns in transformed dataframe is not as expected"

# Test for correct columns in the transformed data
def test_data_preprocessor_columns():
    result = data_preprocessor(drop_feat_1, passthrough_feat_1, categorical_feat_1, numerical_feat_1)
    result.fit_transform(dataframe_1)
    assert result.get_feature_names_out().tolist() == encoded_dataframe_1.columns.tolist(), "Columns in transformed dataframe are not as expected"

# Test for correct error handling for incorrect object type 
def test_data_preprocessor_value_error():
    with pytest.raises(ValueError):
        data_preprocessor(passthrough_feats=passthrough_feat_1_val).fit(dataframe_1)
    with pytest.raises(ValueError):
        data_preprocessor(categorical_feats=categorical_feat_1_val).fit(dataframe_1)
    with pytest.raises(ValueError):
        data_preprocessor(numerical_feats=numerical_feat_1_val).fit(dataframe_1)
    with pytest.raises(ValueError):
        data_preprocessor(numerical_feats=numerical_feat_1_val).fit(dataframe_1_list)

# Test for correct error handling for non-numeric columns into numerical transformer
def test_data_preprocessor_error_non_numeric_columns():
    with pytest.raises(ValueError):
        data_preprocessor(numerical_feats=categorical_feat_1).fit(dataframe_1)