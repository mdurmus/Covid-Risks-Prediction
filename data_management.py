import streamlit as st
import pandas as pd

@st.cache_data
def load_covid_data():
    file_path = "inputs/dataset/Covid Data.csv"
    df = pd.read_csv(file_path)
    return df