import pandas as pd
import numpy as np
import pytest
import sys
import os

# Import the read_melt_merge function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.read_melt_merge import read_melt_merge

# Test data
# mock data files are in the data folder in tests folder

# Expected outputs
three_df_output = pd.DataFrame(np.array([
        ['Canada',2020,0.895534,  0.634954,     0.612844],
        ['China',  2020,  0.625376,  0.142219,  0.021249],
        ['India',  2020,  0.276151,  0.886281,  0.282954],
        ['US',  2020,  0.899793,  0.397402,       np.nan],
        ['Canada',  2021,  0.737636,  0.097864,  0.257960],
        ['China',  2021,  0.828379,  0.715054,  0.842732],
        ['India',  2021,  0.628880,  0.557298,  0.096315],
        ['US',  2021,  0.627453,  0.454399,       np.nan],
        ['Canada',  2022,  0.788306,  0.775559,  0.480900],
        ['China',  2022,  0.947178,  0.216303,  0.598200],
        ['India',  2022,  0.872477,  0.931291,  0.892539],
        ['US',  2022,  0.877383,  0.995563,       np.nan],
        ['Canada',  2023,  0.209287, np.nan,       np.nan],
        ['China',  2023,  0.971888,  np.nan,       np.nan],
        ['India',  2023,  0.659193,  np.nan,       np.nan],
        ['US',  2023,  0.132662,     np.nan,       np.nan],
    ]),
    columns=['country','year','col1','col2','col3']#,
    #dtype=[('country', "object"), ('year', "object"), ('col1', "float"), ('col2', "float"), ('col3', "float")]
    )
three_df_output = three_df_output.astype({'country': 'object' ,'year': 'object' ,'col1': 'float' ,'col2': 'float' ,'col3': 'float'})

# Test inputs
three_files=['mock_data_1','mock_data_2','mock_data_3']
three_cols=['col1','col2','col3']
two_files=['mock_data_1','mock_data_2']
two_cols=['col1','col2']
one_file=['mock_data_1']
one_col=['col1']

three_files_dict={'mock_data_1','mock_data_2','mock_data_3'}
three_cols_tuple=('col1','col2','col3')


# Test for correct return type
def test_read_melt_merge_returns_dataframe():
    data_files_names = ['mock_data_1','mock_data_2','mock_data_3']
    col_names = ['col1','col2','col3']
    merged_df = read_melt_merge(data_files_names, col_names, path='tests/data/', id_variable='country', variable_name='year')
    assert isinstance(merged_df, pd.DataFrame), "read_melt_merge` should return a pandas data frame"

# Test for correct number of columns in the output
def test_read_melt_merge_number_of_columns():
    assert read_melt_merge(three_files, three_cols, path='tests/data/').shape[1] == 2+len(three_files)
    assert read_melt_merge(two_files, two_cols, path='tests/data/').shape[1] == 2+len(two_files)
    assert read_melt_merge(one_file, one_col, path='tests/data/').shape[1] == 2+len(one_file)

# Test for correct values in the data frame
def test_count_classes_count_values():
    pd.testing.assert_frame_equal(read_melt_merge(three_files, three_cols, path='tests/data/'), three_df_output)


# Test for correct error handling for incorrect type of column value 
def test_read_melt_merge_type_error():
    with pytest.raises(FileNotFoundError):
        read_melt_merge(three_files, three_cols, path='1')
    with pytest.raises(TypeError) :
        read_melt_merge(three_files, three_cols, path='tests/data/',id_variable='country', variable_name=1)
    with pytest.raises(KeyError):
        read_melt_merge(three_files, three_cols, path='tests/data/',id_variable=1)
    with pytest.raises(TypeError):
        read_melt_merge(three_files_dict, three_cols, path='tests/data/')
