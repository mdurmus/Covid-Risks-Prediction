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