# reading data sets, melting data from wide table to long table in Data Wrangling Section and merging dataframes.

import pandas as pd


def read_melt_merge(data_files_names, col_names, path='../data/raw/', id_variable='country', variable_name='year'):
    """
    Read csv files to create pandas DataFrames.

    Melt wide pandas DataFrames from wide table to long table.

    Merge melted pandas DataFrames.

    Parameters:
    ----------
    data_files_names : the name of data file name
        The input should be a list that contains at least one name.
    col_names :
        The column names to store the values of each melted pandas DataFrames.
    path :
        path to the raw data files.
    id_variable : str
        The name of the column in the DataFrame to melt table.
    variable_name : str
        The name of the column in the DataFrame to melt table.

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with at least four columns:
        - id_variable: categorical column in melted pandas DataFrame, which is used to merge data.
        - variable_name: categorical column in melted pandas DataFrame, which is used to merge data.
        - col_names: several columns that store the value of melted pandas DataFrames.
        
    Examples:
    --------
    >>> import pandas as pd
    >>> data_files_names = ['co2_emissions_tonnes_per_person','coal_consumption_per_cap']  # Replace list with the charaterical values of your data file names.
    >>> col_names = ['co2_e', 'coal_c'] #replace list with names of columns that store the data of melted DataFrames.
    >>> merged_df = read_melt_merge(data_file_names, col_names)
    >>> print(merged_df)
    
    Notes:
    -----
    This function uses the pandas library to perform read, melt and merge values in the input DataFrame.

    """
    # Read Data
    sub_df_list = []
    for i in range(len(data_files_names)):
        file_name = data_files_names[i]
        sub_df = pd.read_csv(f"{path}{file_name}.csv").melt(id_vars=id_variable, var_name=variable_name, value_name=col_names[i])
        sub_df_list.append(sub_df)
    
    merged_df = sub_df_list[0]
    for df in sub_df_list[1:]:
    # Merge each DataFrame with the merged DataFrame
        merged_df = pd.merge(merged_df, df, on=[id_variable,variable_name], how ='outer')
    return merged_df
