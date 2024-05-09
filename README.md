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
| MEDICAL_UNIT | The type of National Health institution providing patient care and treatment.
 | 1-13 |
| CLASIFFICATION_FINAL | Covid test results. | 1-7 |

