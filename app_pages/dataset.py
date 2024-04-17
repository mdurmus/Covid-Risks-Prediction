import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import seaborn as sns

def load_dataset(file_path):
    df=pd.read_csv(file_path)
    return df

def dataset_body():
    """ Page 2 contents"""
    st.set_option('deprecation.showPyplotGlobalUse',False)
    st.write('## Dataset')
    st.markdown('<p>The dataset was provided by the Mexican government and is sourced from Kaggle. This dataset contains an enormous number of anonymized patient-related information including pre-conditions. The raw dataset consists of 21 unique features and 1,048,576 unique patients. In the Boolean features, 1 means "yes" and 2 means "no". values as 97 and 99 are missing data. </p>',unsafe_allow_html=True)
    file_path = "inputs/dataset/Covid Data.csv"
    df = load_dataset(file_path)
    st.write('Size of the dataset: ', df.shape)

    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(97, 2)
    df['PREGNANT'] = df['PREGNANT'].astype('float64')
    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(98, np.nan)
    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(2, 0)

    var = df.columns[(df.nunique() == 3) | (df.nunique() == 4)].tolist()
    df.loc[:, var] = df.loc[:, var].replace([97, 98, 99], np.NAN)
    df.loc[:, var] = df.loc[:, var].replace(2, 0)

    df['DIED'] = np.where(df['DATE_DIED'] == '9999-99-99', 0, 1)
    df.drop(columns='DATE_DIED', inplace=True)

    line_add()

    #st.write('Percentage of NAN values')

    #for col in df.columns :
    #    st.write('{:<20} => {:>10.2f}%'.format(col, df[col].isna().sum()/len(df)*100))

    st.write('<h3 style="color:red;">Percentage of NAN values</h3>', unsafe_allow_html=True)

    nan_percentage_data = {'Column': [], 'NaN Percentage': []}
    for col in df.columns:
        nan_percentage = df[col].isna().sum() / len(df) * 100
        nan_percentage_data['Column'].append(col)
        nan_percentage_data['NaN Percentage'].append('{:.2f}%'.format(nan_percentage))

    nan_percentage_df = pd.DataFrame(nan_percentage_data)
    st.table(nan_percentage_df)
    

    line_add()

    st.write('### Data Summary')
    st.markdown('<p>We are displaying the summary of the dataset. The first five rows show the beginning and content of the dataset. This shows which columns make up the dataset, the first five rows of each column, and the data types found in these rows. This information provides a quick overview of the dataset\'s contents and can help in deciding which columns to select for further analysis.</p>',unsafe_allow_html=True)

    st.write(df.head())
    line_add()



    st.write('### Access Data')
    st.markdown('<p>In the "Access Data" section, users are provided with the option to select specific columns from the dataset. A multiselect dropdown menu is presented where users can choose one or more columns they are interested in. Once the columns are selected, the corresponding data from those columns is displayed in a table format below the dropdown menu. This allows users to focus on specific columns of interest and explore their data further.</p>',unsafe_allow_html=True)
    selected_columns = st.multiselect('Select Column: ',df.columns)
    if selected_columns:
        st.write(df[selected_columns])
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


    line_add()
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