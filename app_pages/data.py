import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import seaborn as sns
from data_management import load_covid_data

def data_body():
    """ Page 2 contents"""
    df = load_covid_data()
    st.set_option('deprecation.showPyplotGlobalUse',False)    
    st.write('### Data Summary')
    st.markdown('<p>We are displaying the summary of the dataset. The first five rows show the beginning and content of the dataset. This shows which columns make up the dataset, the first five rows of each column, and the data types found in these rows. This information provides a quick overview of the dataset\'s contents and can help in deciding which columns to select for further analysis.</p>',unsafe_allow_html=True)

    st.write(df.head())
    line_add()
    

    st.write('### Access Data')
    st.markdown('<p>In the "Access Data" section, users are provided with the option to select specific columns from the dataset. A multiselect dropdown menu is presented where users can choose one or more columns they are interested in. Once the columns are selected, the corresponding data from those columns is displayed in a table format below the dropdown menu. This allows users to focus on specific columns of interest and explore their data further.</p>',unsafe_allow_html=True)

    option = st.selectbox(
    "Number Records",
    (10, 50, 100, 1000000),
    index=None,
    placeholder="Number of Records")
    disabled = option is None
    selected_columns = st.multiselect('Select Column: ',df.columns, disabled=disabled)
    if selected_columns:
        st.write(df[selected_columns].head(option))
    line_add()
    
    
    st.write('### Statistical Data')
    st.markdown('<p>In the "Statistical Data" section, descriptive statistics of the dataset are presented. This includes measures such as count, mean, standard deviation, minimum, quartiles, and maximum values for each numerical column in the dataset. These statistics offer insights into the central tendency, dispersion, and distribution of the data. Users can use this information to understand the overall characteristics of the dataset and identify any patterns or outliers.</p>',unsafe_allow_html=True)
    st.write(df.describe())   
    line_add()


    st.write('### Data Visulation')
    st.markdown('<p>In the "Data Visualization" section, a graphical representation of the data is provided. Users are presented with a dropdown menu where they can select a column of interest from the dataset. Once a column is selected, a histogram plot is generated, displaying the distribution of values within that column. This visualization helps users to visually explore the data distribution, identify trends, patterns, or anomalies, and gain insights into the underlying data characteristics.</p>',unsafe_allow_html=True)
    selected_column_hist = st.selectbox("Select Column: ", df.columns)
    plt.hist(df[selected_column_hist], bins=20)
    st.pyplot()

def line_add():
    st.markdown("""<hr style="border: 0;
                              height: 1px;
                              background: #333;
                              background-image: linear-gradient(to right, #ccc, #333, #ccc);" /> 
                """, unsafe_allow_html=True)