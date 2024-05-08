import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import seaborn as sns
import pickle
from data_management import load_covid_data
from sklearn.preprocessing import RobustScaler

def check_body():
    '''
    Check body contents
    '''
    st.write('Please enter your options')

    scaler = RobustScaler()

    # Load the ML model
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    # Define feature names (excluding target)
    features = [
        "USMER","SEX","PATIENT_TYPE","PNEUMONIA","AGE","DIABETES","COPD","HIPERTENSION","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","RENAL_CHRONIC","MEDICAL_UNIT","CLASIFFICATION_FINAL"
    ]

    # Create checkboxes for feature selection
    selected_features = st.multiselect("Select Features:", features, default=features)

    # Display user input section
    user_input = {}
    for feature in selected_features:
        if feature in ["AGE"]:  # Handle numerical features (adjust data types)
            user_in = st.number_input(f"Enter {feature}:")
            user_input[feature] = scaler.transform([[user_in]])[0][0]

        #one hot encoded feature
        elif feature == "CLASIFFICATION_FINAL":
            # Radio buttons for one-hot encoding
            classification_final_value = st.radio(
                "Select CLASIFFICATION_FINAL:",
                ("1", "2", "3", "4", "5", "6", "7"),
                horizontal=True
            )
            # Create one-hot encoded representation based on selection (assuming 0 for not selected)
            user_input["CLASIFFICATION_FINAL_1"] = float(classification_final_value == "1")
            user_input["CLASIFFICATION_FINAL_2"] = float(classification_final_value == "2")
            user_input["CLASIFFICATION_FINAL_3"] = float(classification_final_value == "3")
            user_input["CLASIFFICATION_FINAL_4"] = float(classification_final_value == "4")
            user_input["CLASIFFICATION_FINAL_5"] = float(classification_final_value == "5")
            user_input["CLASIFFICATION_FINAL_6"] = float(classification_final_value == "6")
            user_input["CLASIFFICATION_FINAL_7"] = float(classification_final_value == "7")

        #one hot encoded feature
        elif feature == "MEDICAL_UNIT":
            # Radio buttons for one-hot encoding
            classification_final_value = st.radio(
                "Select MEDICAL_UNIT:",
                ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"),
                horizontal=True
            )
            # Create one-hot encoded representation based on selection (assuming 0 for not selected)
            user_input["MEDICAL_UNIT_1"] = float(classification_final_value == "1")
            user_input["MEDICAL_UNIT_2"] = float(classification_final_value == "2")
            user_input["MEDICAL_UNIT_3"] = float(classification_final_value == "3")
            user_input["MEDICAL_UNIT_4"] = float(classification_final_value == "4")
            user_input["MEDICAL_UNIT_5"] = float(classification_final_value == "5")
            user_input["MEDICAL_UNIT_6"] = float(classification_final_value == "6")
            user_input["MEDICAL_UNIT_7"] = float(classification_final_value == "7")
            user_input["MEDICAL_UNIT_8"] = float(classification_final_value == "8")
            user_input["MEDICAL_UNIT_9"] = float(classification_final_value == "9")
            user_input["MEDICAL_UNIT_10"] = float(classification_final_value == "10")
            user_input["MEDICAL_UNIT_11"] = float(classification_final_value == "11")
            user_input["MEDICAL_UNIT_12"] = float(classification_final_value == "12")
            user_input["MEDICAL_UNIT_13"] = float(classification_final_value == "13")

        elif feature == "SEX": #feature == "USMER"or feature == "PATIENT_TYPE"
            #user_input[feature] = st.selectbox(f"Select {feature}:", [1.0, 2.0])
           
            # Define options and corresponding values
            gender_map = {"Female": 1.0, "Male": 2.0}

            # Create the selectbox with a default selection (optional)
            selected_gender = st.selectbox("Select Gender:", list(gender_map.keys()), index=0)

            # Get gender value using dictionary lookup (avoiding if-else)
            gender_value = gender_map.get(selected_gender, 0.0)  # Default value if not found

            # Use the gender_value variable in your code
            user_input[feature] = gender_value

        elif feature == "PATIENT_TYPE":
            patient_type_map = {"Returned Home": 1.0, "Hospitalization": 2.0}

            # Create the selectbox with a default selection (optional)
            selected_patient_type = st.selectbox("Select Patient Type:", list(patient_type_map.keys()), index=0)

            # Get gender value using dictionary lookup (avoiding if-else)
            patient_type_value = patient_type_map.get(selected_patient_type, 1.0)  # Default value if not found

            # Use the gender_value variable in your code
            user_input[feature] = patient_type_value
        
        elif feature == "PNEUMONIA":
            # Clarify presence/absence (binary classification)
            pneumonia_options = {"No": 0.0, "Yes": 1.0}

            # Create the selectbox with a clear prompt
            selected_pneumonia = st.selectbox("Does the patient have Pneumonia?", list(pneumonia_options.keys()), index=0)

            # Get pneumonia value using dictionary lookup
            pneumonia_value = pneumonia_options.get(selected_pneumonia, None)  # Handle invalid selections gracefully

            # Validate user input (optional)
            if pneumonia_value is None:
                st.error("Please select a valid option for Pneumonia.")
            else:
                user_input[feature] = pneumonia_value

        elif feature == "DIABETES":
            diabetes_options = {"No": 0.0, "Yes":1.0}
            selected_diabetes = st.selectbox("Does the patient have Diabetes?", list(diabetes_options.keys()), index=0)
            diabetes_value = diabetes_options.get(selected_diabetes, None)
            if diabetes_value is None:
                st.error("Please select a valid option for Diabetes.")
            else:
                user_input[feature] = diabetes_value

        elif feature == "COPD":
            copd_options = {"No": 0.0, "Yes":1.0}
            selected_copd = st.selectbox("Does the patient have COPD?", list(copd_options.keys()), index=0)
            copd_value = copd_options.get(selected_copd, None)
            if copd_value is None:
                st.error("Please select a valid option for COPD.")
            else:
                user_input[feature] = copd_value
        
        elif feature == "HIPERTENSION":
            hipertension_options = {"No": 0.0, "Yes":1.0}
            selected_hipertension = st.selectbox("Does the patient have hypertension?", list(hipertension_options.keys()), index=0)
            hipertension_value = hipertension_options.get(selected_hipertension, None)
            if hipertension_value is None:
                st.error("Please select a valid option for Hipertension.")
            else:
                user_input[feature] = hipertension_value

        elif feature == "OTHER_DISEASE":
            other_disease_options = {"No": 0.0, "Yes":1.0}
            selected_other_disease = st.selectbox("Does the patient have any other disease?", list(other_disease_options.keys()), index=0)
            other_disease_value = other_disease_options.get(selected_other_disease, None)
            if other_disease_value is None:
                st.error("Please select a valid option for other disease.")
            else:
                user_input[feature] = other_disease_value

        elif feature == "CARDIOVASCULAR":
            cardiovascular_options = {"No": 0.0, "Yes":1.0}
            selected_cardiovascular = st.selectbox("Do you have any cardiovascular conditions?", list(cardiovascular_options.keys()), index=0)
            cardiovascular_value = cardiovascular_options.get(selected_cardiovascular, None)
            if cardiovascular_value is None:
                st.error("Please select a valid option for cardiovascular disease.")
            else:
                user_input[feature] = cardiovascular_value

        elif feature == "OBESITY":
            obesity_options = {"No": 0.0, "Yes":1.0}
            selected_obesity = st.selectbox("Do you have any Obesity conditions?", list(obesity_options.keys()), index=0)
            obesity_value = obesity_options.get(selected_obesity, None)
            if obesity_value is None:
                st.error("Please select a valid option for obesity disease.")
            else:
                user_input[feature] = obesity_value

        elif feature == "RENAL_CHRONIC":
            renal_chronic_options = {"No": 0.0, "Yes":1.0}
            selected_renal_chronic = st.selectbox("Do you have any Renal Chronic?", list(renal_chronic_options.keys()), index=0)
            renal_chronic_value = renal_chronic_options.get(selected_renal_chronic, None)
            if renal_chronic_value is None:
                st.error("Please select a valid option for renal disease.")
            else:
                user_input[feature] = renal_chronic_value
        
        

        else:  # Handle categorical features (adjust based on encoding)
            user_input[feature] = st.selectbox(f"Select {feature}:", [0.0, 1.0])

    # Create a button to trigger prediction
    predict_button = st.button("Predict Mortality Risk")

    # Prediction logic (conditional)
    if predict_button:
        # Prepare user input as a list or NumPy array
        X = [user_input["USMER"], user_input["SEX"], user_input["PATIENT_TYPE"], user_input["PNEUMONIA"], user_input["AGE"], user_input["DIABETES"], user_input["COPD"], user_input["HIPERTENSION"], user_input["OTHER_DISEASE"], user_input["CARDIOVASCULAR"], user_input["OBESITY"], user_input["RENAL_CHRONIC"], user_input["MEDICAL_UNIT_1"], user_input["MEDICAL_UNIT_2"], user_input["MEDICAL_UNIT_3"], user_input["MEDICAL_UNIT_4"], user_input["MEDICAL_UNIT_5"], user_input["MEDICAL_UNIT_6"], user_input["MEDICAL_UNIT_7"], user_input["MEDICAL_UNIT_8"], user_input["MEDICAL_UNIT_9"], user_input["MEDICAL_UNIT_10"], user_input["MEDICAL_UNIT_11"], user_input["MEDICAL_UNIT_12"], user_input["MEDICAL_UNIT_13"], user_input["CLASIFFICATION_FINAL_1"], user_input["CLASIFFICATION_FINAL_2"],user_input["CLASIFFICATION_FINAL_3"], user_input["CLASIFFICATION_FINAL_4"], user_input["CLASIFFICATION_FINAL_5"], user_input["CLASIFFICATION_FINAL_6"], user_input["CLASIFFICATION_FINAL_7"]]

        st.write(X)


        X = np.array([X])  # Convert to a 2D array for prediction (adjust if needed)

        # Make prediction using the loaded model
        prediction = model.predict(X)[0]  # Assuming binary classification

        # Display the prediction result
        st.write(f"The Patient will probably: {"die" if prediction else "live"}")  # Format probability


def line_add():
    st.markdown("""<hr style="border: 0;
                              height: 1px;
                              background: #333;
                              background-image: linear-gradient(to right, #ccc, #333, #ccc);" /> 
                """, unsafe_allow_html=True)