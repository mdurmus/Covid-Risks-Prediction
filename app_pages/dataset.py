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
    st.write('### Dataset')
    st.write(f'''
                The dataset was provided by the Mexican government and is sourced from Kaggle. 
                This dataset contains an enormous number of anonymized patient-related information 
                including pre-conditions. The raw dataset consists of 21 unique features and 1,048,576 
                unique patients. In the Boolean features, 1 means "yes" and 2 means "no". values as 97 
                and 99 are missing data.''')

    df = load_covid_data()

    st.write(f"""<p style="font-size:20px;color:#A3FFD6;">Size of the dataset: <span style='font-weight:bold;font-size:22px;'>{df.shape} </span></p>""",unsafe_allow_html=True)

    line_add()
    st.write('### Data Cleaning & Transformation')
    st.write("##### Correcting Pregnancy Values by Gender & Converting Boolean Values")
    st.write(f'''
                We see that all males have value 97 for pregnancy because it is missing. Given that 
                males cannot get pregnant, we will change all 97's in PREGNANT to 2. Some females have 98 
                which is a missing value, so we change all the 98's in PREGNANT to NAN. Currently 1 represents 
                True and 2 represents False. To change the boolean values to the conventional way, we change 
                the 2's to 0's.''')

    st.markdown(f'''<code>
        df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(97, 2)
df['PREGNANT'] = df['PREGNANT'].astype('float64')
df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(98, np.nan)
df.loc[:, 'PREGNANT'] = df.loc[:, 'PREGNANT'].replace(2, 0)
    </code>''', unsafe_allow_html=True)
   

    line_add()
    st.write("##### Data Cleaning & Transformation: Rectifying and Converting Boolean Values")
    st.write(f'''
                Some columns contain 3-4 unique values when it should be a boolean: YES or NO. 
                We replace all 97's, 98's, and 99's to NAN because they are missing values. 
                The 1's mean YES and 2's mean NO, so we change 2's to 0's, the conventional way to #
                represent Boolean values.''')

    st.markdown(f'''<code>
var = df.columns[(df.nunique() == 3) | (df.nunique() == 4)].tolist()
df.loc[:, var] = df.loc[:, var].replace([97, 98, 99], np.NAN)
df.loc[:, var] = df.loc[:, var].replace(2, 0)
                    </code>''', unsafe_allow_html=True)
   

    line_add()

    st.write("##### Transformation of DATE_DIED Values Based on Survival Status")
    st.write(f'''
                DATE_DIED is represent as a pandas date format of when the patient died. If we have 9999-99-99 
                values, that means this patient is alive. Since our goal is to build models that predict surival 
                rate given a patient's characteristics, we will change the DATE_DIED to 0 if the patient is alive 
                or 1 if the patient died.''')

    st.markdown(f'''<code>
df['DIED'] = np.where(df['DATE_DIED'] == '9999-99-99', 0, 1)
df.drop(columns='DATE_DIED', inplace=True)
    </code>''', unsafe_allow_html=True)

    line_add()

    st.write("##### Correlation Test and Feature Extraction")
    st.write(f'''
                To extract the features that has the lowest correlation with the column DIED, 
                we made a correlation test.''')

    st.markdown(f'''<code>
correlation_matrix = df.corr()
target_variable = 'DIED'
correlation_with_target = correlation_matrix[target_variable]
sorted_correlation = correlation_with_target.abs().sort_values()
lowest_4_features = sorted_correlation.head(4).index      
                    </code>''', unsafe_allow_html=True)

    st.write(f"""
                According to correlation test, we found out these 4 features with 
                lowest correlation with 'DIED' column""")

    st.markdown(f'''<code>
Lowest 4 correlated features with DIED :
Index(['TOBACCO', 'ASTHMA', 'PREGNANT', 'INMSUPR'], dtype='object')  
                    </code>''', unsafe_allow_html=True)

    st.write(f"""
                Thus, we will drop the features that have low correlation with DIED feature.""")

    st.markdown(f'''<code>
df.drop(columns=lowest_4_features, inplace=True)
                    </code>''', unsafe_allow_html=True)




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
    st.write(f"""<p style="color:white;">Variables in our dataset are as follows. 
    After the mentioned operations are completed, the total number of remaining 
    variables is 21.</p>""",unsafe_allow_html=True)
    columns = df.columns.tolist()
    st.write(columns)
   


def line_add():
    st.markdown("""<hr style="border: 0;
                              height: 1px;
                              background: #333;
                              background-image: linear-gradient(to right, #ccc, #333, #ccc);" /> 
                """, unsafe_allow_html=True)