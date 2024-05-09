import streamlit as st


def home_body():
    """ Home page contents"""
    st.write("## Welcome to Corona Risk Prediction")
    st.markdown(f"""<div style="
                        background-color:#ffeeeb; 
                        padding:30px; 
                        margin-top:15px;
                        border-radius: 5px;
                        text-align: left;
                        border:2px solid red;">
    This platform is designed to classify at-risk COVID patients using an artificial intelligence model developed 
    during the COVID-19 pandemic. Our goal is to assess patients\' health conditions and identify potential risk 
    factors by utilizing this AI model.</div>""", unsafe_allow_html=True)
    st.write("## Dataset")
    dataset()
    st.write("")
    st.markdown(f"""<span style="font-size:20px;color:white;">
    For additional information, please click <a href='https://github.com/mdurmus/Covid-Risks-Prediction/blob/main/README.md' target='_blank'>here</a>.</span>""", unsafe_allow_html=True)
    
    business()



def dataset():
    dataset = st.empty()
    dataset.markdown(f'''<div style="background-color:#ffeeeb; 
                                     padding:30px; 
                                     margin-top:15px;
                                     border-radius: 5px;
                                     text-align: left;
                                     border:2px solid red;">
    The dataset was provided by the Mexican government and is sourced from <a href="https://www.kaggle.com/code/addicejeremy/classifying-at-risk-covid-patients/notebook" target="_blank">Kaggle</a>. 
    This dataset contains an enormous number of anonymized patient-related information including pre-conditions. 
    The raw dataset consists of 21 unique features and 1,048,576 unique patients.
                    </div>''', unsafe_allow_html=True)

def business():
    st.write("## Business Case")
    business = st.empty()
    business.markdown(f'''<div style="background-color:#198754;
                                      padding:30px; 
                                      margin-top:15px;
                                      border-radius: 5px;
                                      text-align: left;
                                      border:2px solid brown;
                                      color:white;
                                      font-size:19px;
                                      line-height:28px;">
A project addressing the shortage of healthcare resources and lack of an efficient distribution plan during the Covid-19 pandemic. 
A machine learning model aims to identify high-risk individuals by analyzing data such as patients' symptoms, medical history, and test results. 
These predictions guide authorities in identifying potentially high-risk patients and allocating medical resources effectively, thus ensuring better preparedness of healthcare systems.
                                      </div>''', unsafe_allow_html=True)