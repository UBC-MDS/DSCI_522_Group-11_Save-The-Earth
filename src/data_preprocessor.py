# Initialize packages
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer

def data_preprocessor(drop_feats=None, passthrough_feats=None, categorical_feats=None, numerical_feats=None):
    """
    Create Sklearn Column Transformer to drop, passthrough, encode and scale specified features

    Parameters:
    ----------
    drop_feats : list
        The columns to drop in the fitting DataFrame
    passthrough_feats : list
        The columns to passthrough in the fitting DataFrame
    categorical_feats : list
        The columns to encode with Sklearn OneHotEncoder in the fitting DataFrame
    numerical_feats : list
        The columns to scale with Sklearn StandardScaler in the fitting DataFrame

    Returns:
    -------
    sklearn.compose._column_transformer.ColumnTransformer
        A Sklearn Column Transformer to fit and transform the target DataFrame with the specified preprocessors and columns
        
    Examples:
    --------
    >>> preprocessor = data_preprocessor(drop_feats=['col1'], passthrough_feats=['col2'], categorical_feats=['col3'], numerical_feats=['col4'])
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