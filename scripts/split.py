# split.py
# author: Jing Wen
# date: 2023-11-28

import click
import os
import pandas as pd
from sklearn.model_selection import train_test_split

@click.command()
@click.option('--raw_data', type=str, help="Path to raw data")
@click.option('--data_to', type=str, help="Path to directory where processed data will be written to")
@click.option('--random_state', type=int, help="Random state", default=123)

def main(raw_data, data_to, random_state):
    '''This script splits and save the raw data into train and test sets'''

    df = pd.read_csv(raw_data, index_col=0)

    # create the split
    train_df, test_df = train_test_split(
        df, test_size=0.20, random_state=random_state
    )

    train_df.to_csv(os.path.join(data_to, "train_df.csv"), index=True)
    test_df.to_csv(os.path.join(data_to, "test_df.csv"), index=True)

if __name__ == '__main__':
    main()