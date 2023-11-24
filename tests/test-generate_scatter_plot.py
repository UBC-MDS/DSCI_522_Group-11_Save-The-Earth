import pandas as pd
import pytest
import sys
import os
import altair as alt

# Import the create_scatter_plot function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.create_scatter_plot import create_scatter_plot

# Test data
toy_dataset_1 = pd.DataFrame({
    'gas_g': [1.5, 2.1],
    'oil_g': [1.1, 1.9],
    'country': ['A', 'B'],
})

# Test for correct return type
def test_create_scatter_plot_returns_chart():
    result = create_scatter_plot(toy_dataset_1, 'gas_g', 'oil_g', 'country')
    assert isinstance(result, alt.Chart), "`create_scatter_plot` should return an Altair Chart object"

# Test for correct error handling for incorrect type of column value (not a string)
def test_create_scatter_plot_type_error():
    with pytest.raises(TypeError):
        create_scatter_plot(toy_dataset_1, 1, 'oil_g', 'country')

# Test for correct handling of non-string color_field
def test_create_scatter_plot_non_string_color_field():
    with pytest.raises(TypeError):
        create_scatter_plot(toy_dataset_1, 'gas_g', 'oil_g', 123)

# Test for correct handling of negative width and height
def test_create_scatter_plot_negative_dimensions():
    with pytest.raises(ValueError):
        create_scatter_plot(toy_dataset_1, 'gas_g', 'oil_g', 'country', -400, 400)
    with pytest.raises(ValueError):
        create_scatter_plot(toy_dataset_1, 'gas_g', 'oil_g', 'country', 400, -400)

# Test for correct error handling for incorrect object type (not a pandas data frame)
def test_create_scatter_plot_value_error_df():
    with pytest.raises(TypeError):
        create_scatter_plot('toy_dataset_1', 'gas_g', 'oil_g', 'country')