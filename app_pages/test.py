import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import seaborn as sns
from data_management import load_covid_data

def test_body():
    '''Test page icerik'''

    df = load_covid_data()

    st.write('### Correlation Test and Result')
    # Calculate the correlation matrix
    numerical_df = df.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numerical_df.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Generate a heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)

    # Add title and display the plot
    plt.title('Correlation Matrix of Provided Features')
    st.pyplot()
    line_add()

def line_add():
    st.markdown("""<hr style="border: 0;
                              height: 1px;
                              background: #333;
                              background-image: linear-gradient(to right, #ccc, #333, #ccc);" /> 
                """, unsafe_allow_html=True)