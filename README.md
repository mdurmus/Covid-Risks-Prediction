# Covid Risks Prediction

Coronavirus disease (COVID-19) is an infectious disease caused by a recently discovered coronavirus that has affected people worldwide. Most individuals infected with the coronavirus, including young and healthy individuals, experience mild to moderate respiratory symptoms and recover without requiring special treatment. However, elderly individuals and those with underlying medical conditions such as cardiovascular diseases, diabetes, chronic respiratory diseases, and cancer are at a higher risk of developing severe complications. For these individuals, these complications could even lead to fatalities.

One of the main challenges faced by healthcare providers during the pandemic is the shortage of medical resources and the lack of an effective plan for their distribution. Being able to predict in advance what type of resources an individual may need during challenging times and directing resources accordingly is the primary goal of our project.

![Covid Risk Prediction](readme/intro.png)

[Covid Risk Prediction Live Application](https://covid-predictors-0ff909d85a90.herokuapp.com/)

[Covid Risk Project User Stories](https://github.com/users/mdurmus/projects/7/views/1)

## Dataset Content

The source of this dataset is the [Kaggle](https://www.kaggle.com/datasets/meirnizri/covid19-dataset) website. The dataset has been provided by the Mexican government. Originally, it consists of 21 features and a total of 1,048,576 patient records. However, due to feature engineering efforts, the number of features has been reduced to 16. You can find relevant explanations on the project page.

| Variable | Meaning  | Units    |
|----------|----------|----------|
| USMER  | The variable that indicates whether the patient has received COVID treatment before. | Yes, No  |
| SEX  | The variable that stores the gender of the patient.  | Male, Female  |
| PATIENT_TYPE  | The variable that stores whether the patient's treatment should be done at home or in the hospital.  | Returned Home, Hospitalization  |
| PNEUMONIA | The variable that stores the presence of pneumonia in the patient. | Yes, No |
| AGE | The variable that stores the age information of the patient. | Numeric |
| DIABETES | The variable that stores whether the patient has diabetes or not. | Yes, No |
| COPD | The variable that stores whether the patient has COPD (Chronic Obstructive Pulmonary Disease) or not. | Yes, No |
| HIPERTENSION | The variable that stores whether the patient has hypertension or not. | Yes, No |
| OTHER_DISEASE | The variable that stores whether the patient has any other condition or not. | Yes, No |
| CARDIOVASCULAR | The variable that stores whether the patient has cardiovascular disease or not. | Yes, No |
| OBESITY | The variable that stores whether the patient is obese or not. | Yes, No |
| RENAL_CHRONIC | The variable that stores whether the patient has a chronic kidney condition or not. | Yes, No |
| MEDICAL_UNIT | The type of National Health institution providing patient care and treatment. | 1-13 |
| CLASIFFICATION_FINAL | Covid test results. | 1-7 |

## Business Requirements

The AI-based Covid risks prediction project will collect and integrate Covid-19 test results and symptom data from healthcare institutions and other sources. These data will be analyzed by a risk scoring algorithm and presented to users via a user interface. The project will encompass ensuring the security and privacy of user data, compliance with GDPR and similar legal regulations, scalability and performance, authentication and authorization processes, transmission and monitoring of results, and regular system maintenance.

This AI-driven Covid risks prediction software will serve as a fast and effective Covid-19 monitoring and control tool for governments and healthcare institutions. It will provide significant support in identifying and guiding high-risk individuals to healthcare systems. Additionally, it will help create a secure environment for businesses and communities, thus aiding in preventing the spread of the pandemic. Individuals will be informed about their health status, enabling them to track and protect themselves, making them more aware and effective in combating the pandemic.

## Hypothesis and Validation

### Hypothesis

The hypothesis of the AI-based Covid risk prediction project is that it can accurately and reliably predict individuals' Covid-19 risk using Covid-19 test results and symptom data, thereby assisting healthcare institutions in effectively identifying high-risk individuals and guiding treatment.

### Validation

The validation method involves evaluating the performance of the software on real-world data, particularly assessing its ability to accurately identify high-risk individuals. Furthermore, its effectiveness in guiding healthcare institutions and receiving feedback from them will be assessed to iterate and improve the software.

## ML Based Disease Concerns Addressing Application

### Model Evaluation and Feature Selection

I used the scikit-learn library for optimizing model parameters. There is a need for an application that works with a machine learning-based classification system to address the concerns of each individual in the public regarding the disease.

I used the correlation test to understand the relationships between variables in my dataset and to identify which variables are correlated. Additionally, the results of this test helped me understand the relationships between variables. Understanding the relationships between variables also facilitated my feature selection process.

- Training Accuracy Score: 0.9626941603535738
- Testing Accuracy Score: 0.9328095221847994
- F1 Score: 0.48611369990680336
- Confusion Matrix: Overall, the predicted values are close to the true values. The highest accuracy rate is 90.10%, and the lowest accuracy rate is 3.18%.
- Decision Tree ROC Curve: The slope is quite high, indicating that the model performs well. The curve starts from the bottom left corner and extends to the top right corner. This indicates that the model achieves high accuracy at all threshold values.

You can access the details of these tests from the Test Results page within the project.

## ML Business Case

### Business Requirements

1. The customer wants to see how data related to COVID-19, such as disease symptoms and test results, can be gathered and analyzed. 

2. The customer also wants to develop a model capable of predicting COVID-19 cases.

### Business Goal Addressable with Traditional Data Analysis

We can explore the relationships between specific symptoms associated with COVID-19 and test results.

### Dashboard or API Endpoint Need

The customer wants to track COVID-19 cases through a dashboard interface.

### Successful Project Outcome

Delivering a study on significant determinants related to COVID-19. Additionally, developing a model capable of predicting COVID-19 cases.

### Project Epics and User Stories

- Information gathering and data collection: Gathering data associated with COVID-19 cases.

- Data visualization, cleaning, and preparation: Visualizing data, cleaning it, and preparing it for modeling.

- Model training, optimization, and validation: Developing and optimizing a model to predict COVID-19 cases.

- Dashboard planning, design, and development: Creating a dashboard that visualizes COVID-19 cases.

- Dashboard deployment and release: Making the dashboard ready for use and delivering it to the customer.

### Recommended Model
The data suggests proposing a classification model that can predict COVID-19 cases.

### Model Inputs and Outputs
The inputs are data associated with COVID-19, such as disease symptoms and demographic information. The output includes predicting the likelihood or probability of an individual contracting COVID-19.

### Performance Targets for Predictions
Performance metrics such as accuracy and precision of the model will be used to assess its ability to predict COVID-19 cases.

### Customer Benefits
A model that predicts COVID-19 cases can assist healthcare institutions in disease control and resource management. Additionally, it can serve as an informative tool for the overall health of the community.

## Dashboard Design

1. Project Summary

    - In this screen, I am explaining what the application can be used for and what its goal is.

    - General information about the dataset obtained from Kaggle is provided, including the total number of records and details about the variables.

    - The last paragraph on the relevant page explains why the project was developed, in other words, I am outlining our customers' requests and expectations from us.

2. Dataset Features

    - **Dataset**: In this section, the number of records and variables in the dataset has been specified. After selecting features, I organized some boolean variables according to our business logic and made changes to their values. I also displayed the total number of records in this area.

    - **Data Cleaning** 
    
        - Correcting Pregnancy Values by Gender: In this section, I initially adjusted variables assessing the pregnancy status for females. In the original dataset, some females had values of 98, and some had 97 for this variable, while in some cases, it was observed to be NaN. Logically, a female can either be pregnant or not pregnant; hence, I converted this variable to a boolean type. Since males cannot be pregnant, I decided that it was illogical to use this variable for them and removed it from my dataset.

        - Data Cleaning & Transformation: Some columns had taken values like 97, 98, or 99 instead of boolean values, which was fundamentally illogical. Instead, areas equal to 1 were set to TRUE, and areas equal to 2 were set to FALSE to represent them.

        - Transformation of DATE_DIED Values: The column DATE_DIED represents when the patient died in pandas format. If the value is 9999-99-99, it means the patient is alive. However, in my opinion, this could be represented with a boolean field. So, if the patient is alive, it would take FALSE, and if not, it would take TRUE.

        - Correlation Test and Feature Extraction: In our application, the primary goal is to determine whether an individual is alive or deceased. Therefore, the most important column for us is 'DIED'. I attempted to assess the relationship between my target variable and other variables by calculating correlation matrices on the dataset. This was done as a correlation test.

        As a result, I was quite surprised to see that the following four variables had little to no impact on the outcome:

        ```
        ['TOBACCO', 'ASTHMA', 'PREGNANT', 'INMSUPR']
        ```