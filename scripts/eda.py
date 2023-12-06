# eda.py
# author: Jing Wen
# date: 2023-11-29

import click
import os
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt

@click.command()
@click.option('--train_df', type=str, help="Path to processed training data")
@click.option('--plot_to', type=str, help="Path to directory where the plot will be written to")

def main(train_df, plot_to):
    '''
    Plots the distribution of each feature in the processed training data 
    by data type and country. Also saves the plot.

    Parameters
    ----------
    train_df : str
    A string representing the path to the processed training data in CSV format.

    plot_to : str
    A string representing the path to the directory where the plot will be saved.
    '''

    train_df = pd.read_csv(train_df, index_col=0)

    # Distributions for all numerical columns
    train_df.hist(bins=50, figsize=(20, 15));  
    plt.gcf().suptitle('Histogram of Numeric Columns') 
    
    plt.gcf().savefig(os.path.join(plot_to, "histogram_by_numeric_cols.png"))

    # Distribution for each country
    country_dist = alt.Chart(train_df).mark_bar().encode(
        x = alt.X('year', title = "Year").bin(maxbins=10),
        y=alt.Y('count()', title='Count')
    ).properties(
        width=100,
        height=100,
        title="Available energy consumption data per country"
    ).facet(facet=alt.Facet('country:N', 
                            title="Available energy consumption data per country"), columns=6)

    country_dist.save(os.path.join(plot_to, "histogram_by_country.png"))

if __name__ == '__main__':
    main()