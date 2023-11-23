import altair as alt
import pandas as pd

def create_scatter_plot(df, x_field, y_field, color_field, width=400, height=400):
    """
    Creates a scatter plot using Altair.

    Parameters:
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.
    x_field : str
        The name of the column to use for the x-axis.
    y_field : str
        The name of the column to use for the y-axis.
    color_field : str
        The name of the column to use for color encoding.
    width : int, optional
        The width of the chart. Default is 400.
    height : int, optional
        The height of the chart. Default is 400.

    Returns:
    -------
    altair.vegalite.v4.api.Chart
        An Altair Chart object representing the scatter plot.
        
    Examples:
    --------
    >>> import pandas as pd
    >>> data = pd.read_csv('train_df.csv') 
    >>> chart = create_scatter_plot(data, 'gas_g', 'oil_g', 'country')
    >>> print(chart)

    """
    # Check if width and height are positive
    if width < 0 or height < 0:
        raise ValueError("Width and height must be positive.")

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input should be a pandas DataFrame.")
    
    # Create the scatter plot
    chart = alt.Chart(df).mark_circle().encode(
        x=x_field,
        y=y_field,
        color=color_field
    ).properties(
        width=width,
        height=height
    )
    return chart