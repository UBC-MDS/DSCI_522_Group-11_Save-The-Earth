import click
import os
import numpy as np
import pandas as pd
import pickle
import os

def read_melt_merge(data_files_names, col_names, path='./data/raw/', id_variable='country', variable_name='year'):
    """
    Read csv files to create pandas DataFrames.

    Melt wide pandas DataFrames from wide table to long table.

    Merge melted pandas DataFrames.
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

@click.command()
@click.option('--write-to', type=str, help="Path to directory where raw data will be written to")

def main(write_to):
    """Read, clean and reformat data."""
    data_files_names = [
        "co2_emissions_tonnes_per_person",
        "coal_consumption_per_cap",
        "electricity_generation_per_person",
        "electricity_use_per_person",
        "hydro_power_generation_per_person",
        "nuclear_power_generation_per_person",
        "natural_gas_production_per_person",
        "oil_consumption_per_cap",
        "oil_production_per_person",
    ]
    col_names = [
        "co2_e",
        "coal_c",
        "elec_g",
        "elec_c",
        "hydro_g",
        "nuclear_g",
        "gas_g",
        "oil_c",
        "oil_g",
    ]

    merged_df = read_melt_merge(
        data_files_names, col_names, id_variable="country", variable_name="year"
    )

    #EDA to remove years and countries with too many NaN
    cleaned_df = merged_df.query('not co2_e.isna() and not coal_c.isna() and not elec_c.isna() and not oil_c.isna()')
    # remove rows that co2_e, coal_c, elec_c and oil_c do not have na value. But we think it's acceptable that elec_g, hydro_g, nuclear_g and gas_g have na value. 
    # Filling NaN with 0.
    cleaned_df = cleaned_df.fillna(0)
    cleaned_df = cleaned_df.reset_index().drop(columns='index')

    # covert column data type
    cols_to_convert = cleaned_df.columns[3:8]

    # unify the units, e.g. ug to g; kg to g
    cleaned_df[cols_to_convert] = cleaned_df[cols_to_convert].replace(to_replace=r'(\d+)µ', value=r'\1e-6', regex=True)
    cleaned_df[cols_to_convert] = cleaned_df[cols_to_convert].replace(to_replace=r'(\d+(?:\.\d+)?)k', value=r'\1e3', regex=True)

    cleaned_df[cols_to_convert] = cleaned_df[cols_to_convert].apply(pd.to_numeric)

    cleaned_df.to_csv(f"{write_to}/save_the_earth_processed_data.csv", index=True)

if __name__ == '__main__':
    main()