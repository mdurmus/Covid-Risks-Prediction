import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import seaborn as sns
from data_management import load_covid_data

def dataset_body():
    """ Page 2 contents"""
    st.set_option('deprecation.showPyplotGlobalUse',False)
    st.write('## Dataset')
    st.markdown(f'''<p>The dataset was provided by the Mexican government and is sourced from Kaggle. 
    This dataset contains an enormous number of anonymized patient-related information including pre-conditions. 
    The raw dataset consists of 21 unique features and 1,048,576 unique patients. In the Boolean features, 1 means "yes" 
    and 2 means "no". values as 97 and 99 are missing data. </p>''',unsafe_allow_html=True)

    df = load_covid_data()

    st.write(f"<p>Size of the dataset: <span style='font-weight:bold;'>{df.shape} </span></p>",unsafe_allow_html=True)

    line_add()
    st.write('### Data Cleaning & Transformation')
    st.write("<h5 style='color:pink;'>Correcting Pregnancy Values by Gender & Converting Boolean Values</h5>",unsafe_allow_html=True)
    st.write(f'''We see that all males have value 97 for pregnancy because it is missing. Given that males cannot get pregnant, 
    we will change all 97's in PREGNANT to 2. Some females have 98 which is a missing value, so we change all the 98's in PREGNANT to NAN. 
    Currently 1 represents True and 2 represents False. To change the boolean values to the conventional way, we change the 2's to 0's.''')

    st.markdown(f'''<code>
        df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(97, 2)
        df['PREGNANT'] = df['PREGNANT'].astype('float64')
        df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(98, np.nan)
        df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(2, 0)
    </code>''', unsafe_allow_html=True)
    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(97, 2)
    df['PREGNANT'] = df['PREGNANT'].astype('float64')
    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(98, np.nan)
    df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(2, 0)

    line_add()
    st.write("<h5 style='color:pink;'>Data Cleaning & Transformation: Rectifying and Converting Boolean Values</h5>",unsafe_allow_html=True)
    st.write(f'''Some columns contain 3-4 unique values when it should be a boolean: YES or NO. We replace all 97's, 98's, and 99's to NAN because 
                 they are missing values. The 1's mean YES and 2's mean NO, so we change 2's to 0's, the conventional way to represent Boolean values.''')

    st.markdown(f'''<code>
    var = df.columns[(df.nunique() == 3) | (df.nunique() == 4)].tolist()
    df.loc[:, var] = df.loc[:, var].replace([97, 98, 99], np.NAN)
    df.loc[:, var] = df.loc[:, var].replace(2, 0)
    </code>''', unsafe_allow_html=True)
    var = df.columns[(df.nunique() == 3) | (df.nunique() == 4)].tolist()
    df.loc[:, var] = df.loc[:, var].replace([97, 98, 99], np.NAN)
    df.loc[:, var] = df.loc[:, var].replace(2, 0)

    line_add()

    st.write("<h5 style='color:pink;'>Transformation of DATE_DIED Values Based on Survival Status</h5>",unsafe_allow_html=True)
    st.write(f'''DATE_DIED is represent as a pandas date format of when the patient died. If we have 9999-99-99 values, that means this patient is alive. 
                 Since our goal is to build models that predict surival rate given a patient's characteristics, we will change the DATE_DIED to 0 
                 if the patient is alive or 1 if the patient died.''')

    st.markdown(f'''<code>
    df['DIED'] = np.where(df['DATE_DIED'] == '9999-99-99', 0, 1)
    df.drop(columns='DATE_DIED', inplace=True)
    </code>''', unsafe_allow_html=True)
    df['DIED'] = np.where(df['DATE_DIED'] == '9999-99-99', 0, 1)
    df.drop(columns='DATE_DIED', inplace=True)

    line_add()

    st.write('### Data Accuracy and Missing Values Analysis')

    nan_percentage_data = {'Column': [], 'NaN Percentage': []}
    for col in df.columns:
        nan_percentage = df[col].isna().sum() / len(df) * 100
        nan_percentage_data['Column'].append(col)
        nan_percentage_data['NaN Percentage'].append('{:.2f}%'.format(nan_percentage))
    nan_percentage_df = pd.DataFrame(nan_percentage_data)
    st.table(nan_percentage_df)

    line_add()

    st.write('### Variables in dataset')
    st.write("Variables in our dataset are as follows. After the mentioned operations are completed, the total number of remaining variables is 21.")
    columns = df.columns.tolist()
    st.write(columns)

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