"""
Author: Mrinal Desai
Date: March, 2022
This script holds the function to fetch the data from local directory
"""
import pandas as pd
################################################################

def get_clean_data(path):
    """
    Loads and cleans the data from a given path

    """
    data_df = pd.read_csv(path)
    ################################################################

    columns = data_df.columns
    columns = [col.replace('-', '_') for col in columns]
    data_df.columns = columns
    ################################################################

    data_df = data_df[~data_df.duplicated()]
    data_df.columns = data_df.columns.str.strip()
    ################################################################
    data_df = data_df.applymap(
        lambda s: s.lower() if isinstance(s, str) else s)

    ################################################################

    data_df['salary'] = data_df['salary'].map({' >50k': 1, ' <=50k': 0})
    #data_df['salary']= data_df['salary'].replace(to_replace=" >50k", value='1')
    #data_df['salary']= data_df['salary'].replace(to_replace=" <=50k", value='0')
    y_df = data_df.pop('salary')
    x_df = data_df
    ################################################################
    y_df
    return x_df, y_df
