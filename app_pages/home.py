import streamlit as st


def home_body():
    """ Home page contents"""
    st.write("## Welcome to Corona Risk Prediction")
    st.info(
        f"""This platform is designed to classify at-risk COVID patients using an artificial intelligence model developed during the COVID-19 pandemic. Our goal is to assess patients\' health conditions and identify potential risk factors by utilizing this AI model.""")
    st.success(
        f"""
        Detecting the coronavirus disease would benefit individuals, communities, and nations starting from individuals. Here are some of the benefits of this detection:
        1. Benefits to Individuals:
            * Early Diagnosis: Detecting the coronavirus disease in its early stages can enable individuals to receive prompt treatment. This can reduce the severity of the illness and lower the risk of complications.
            * Isolation and Quarantine: Identifying the disease allows individuals to be isolated from others and quarantine measures to be implemented to prevent the spread of infection.
            * Improvement of Health Status: Diagnosed patients can undergo necessary treatment and care, leading to a quicker recovery process.
        2. Benefits to Communities and Societies:
            * Controlling the Disease: Detecting the disease enables the implementation of measures to control the spread of infection, thereby safeguarding public health.
            * Management of the Outbreak: Disease detection provides real-time data to public health authorities, allowing for the development of effective intervention strategies.
            * Formation of Herd Immunity: Isolating individuals who have tested positive for the disease reduces the risk of transmission, supporting the formation of herd immunity in the community.
        3. Benefits to Nations:
            * Containment of the Outbreak: Individual-level detection of the coronavirus disease contributes to the containment of the outbreak at the national and international levels.
            * Mitigation of Economic Effects: Early detection and control of the disease can mitigate economic losses by reducing treatment and care costs and alleviating the burden on healthcare systems.
            * Management of Travel Restrictions: Detecting the disease facilitates effective management of travel restrictions and minimizes their impact on international mobility.
        
        Detecting the coronavirus disease from individuals to nations is crucial for safeguarding public health and minimizing the impacts of the pandemic. Therefore, technologies such as AI-supported prediction systems for early disease detection play a critical role in accelerating this process and aiding in its effective management.
        """
    )
    st.write("## Dataset")
    dataset()
    st.write("\n")
    st.markdown("<span>For additional information, please click <a href='https://github.com/mdurmus/Covid-Risks-Prediction/blob/main/README.md' target='_blank'>here</a>.</span>", unsafe_allow_html=True)



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
    In the Boolean features, 1 means "yes" and 2 means "no". values as 97 and 99 are missing data.
    </div>''', unsafe_allow_html=True)

