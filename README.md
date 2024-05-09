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

## Matching Business Requirements with Machine Learning Tasks

I used the scikit-learn library for optimizing model parameters. There is a need for an application that works with a machine learning-based classification system to address the concerns of each individual in the public regarding the disease.

I used the correlation test to understand the relationships between variables in my dataset and to identify which variables are correlated. Additionally, the results of this test helped me understand the relationships between variables. Understanding the relationships between variables also facilitated my feature selection process.

- Training Accuracy Score: 0.9626941603535738
- Testing Accuracy Score: 0.9328095221847994
- F1 Score: 0.48611369990680336
- Confusion Matrix: Overall, the predicted values are close to the true values. The highest accuracy rate is 90.10%, and the lowest accuracy rate is 3.18%.
- Decision Tree ROC Curve: The slope is quite high, indicating that the model performs well. The curve starts from the bottom left corner and extends to the top right corner. This indicates that the model achieves high accuracy at all threshold values.