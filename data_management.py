import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_covid_data():
    file_path = "inputs/dataset/Covid Data.csv"
    df = pd.read_csv(file_path)

    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(97, 2)
    df['PREGNANT'] = df['PREGNANT'].astype('float64')
    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(98, np.nan)
    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(2, 0)

    var = df.columns[(df.nunique() == 3) | (df.nunique() == 4)].tolist()
    df[var] = df[var].astype(float)
    df.loc[:, var] = df.loc[:, var].replace([97, 98, 99], np.nan)
    df.loc[:, var] = df.loc[:, var].replace(2, 0)

    df['DIED'] = np.where(df['DATE_DIED'] == '9999-99-99', 0, 1)
    df.drop(columns='DATE_DIED', inplace=True)

    correlation_matrix = df.corr()
    target_variable = 'DIED'
    correlation_with_target = correlation_matrix[target_variable]
    sorted_correlation = correlation_with_target.abs().sort_values()
    lowest_4_features = sorted_correlation.head(4).index
    df.drop(columns=lowest_4_features, inplace=True)

    return df