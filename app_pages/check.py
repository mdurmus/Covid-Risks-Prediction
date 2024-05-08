import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import seaborn as sns
from data_management import load_covid_data


def check_body():
    '''
    Check body contents
    '''
    st.write('Please enter your options')

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    # Create input fields for features based on your model's requirements
    feature1 = st.number_input("Enter Feature 1:", min_value=..., max_value=...)  # Adjust data types
    feature2 = st.text_input("Enter Feature 2:")  # Adjust data types
    # ... add input fields for other features

    # Create a button to trigger prediction
    predict_button = st.button("Predict Label")

    if predict_button:  # Run prediction logic only when the button is clicked
        # Prepare user input as a list or NumPy array (adjust based on your model)
        user_input = [feature1, feature2, ...]  # ... add other features

        # Make prediction using the loaded model
        prediction = model.predict([user_input])[0]  # Assuming single output

        # Display the prediction result
        st.write(f"Predicted Label: {prediction}")

def line_add():
    st.markdown("""<hr style="border: 0;
                              height: 1px;
                              background: #333;
                              background-image: linear-gradient(to right, #ccc, #333, #ccc);" /> 
                """, unsafe_allow_html=True)