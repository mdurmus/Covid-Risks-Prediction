import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import seaborn as sns
from data_management import load_covid_data

def test_body():
    '''Test page icerik'''
    st.set_option('deprecation.showPyplotGlobalUse',False)    
    df = load_covid_data()

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
    st.markdown('''
                <div style="margin:10px;padding:10px;color:white;">
                <h3>Training Accuary</h3>
                <p>
                "Training Accuracy" refers to how successful a machine learning model is on its training dataset. It's typically expressed as the ratio of correctly classified examples to the total number of examples. For instance, for a classification model, training accuracy is calculated by dividing the number of correctly predicted labels by the total number of examples. In other words, it's expressed as a percentage, where the number of correctly predicted examples is divided by the total number of examples.

                Training accuracy indicates how well a model performs on the training data, but it's not sufficient alone to evaluate the model's ability to generalize to real-world data. Hence, other performance metrics such as test accuracy are often used alongside training accuracy. Test accuracy measures how well the model performs on data it hasn't seen before and is generally more important than training accuracy for evaluating a model's performance.
                </p>
                <span style='font-weight:bold;'>0.9626941603535738</span>
                </div>
                ''',unsafe_allow_html=True)
    line_add()
    st.write('')
    st.markdown('''
                <div style="margin:10px;padding:10px;color:white;">
                <h3>Testing Accuracy</h3>
                <p>
                "Testing Accuracy" (Test Accuracy) is a metric that measures how well a machine learning model performs on a test dataset it hasn't been exposed to during training. It's typically expressed as the ratio of correctly classified examples to the total number of examples in the test dataset.

                Testing accuracy indicates how effectively a model generalizes to real-world data, and it's often more critical than training accuracy because it evaluates the model's ability to generalize. A high testing accuracy implies that the model has successfully generalized what it learned during training and can adapt well to new data.
                </p>
                <span style='font-weight:bold;'>0.9328095221847994</span>
                 </div>
                ''',unsafe_allow_html=True)
    line_add()
    st.write('')
    st.markdown('''
                <div style="margin:10px;padding:10px;">
                <h3>F1-Score</h3>
                <p>
                The F1 Score is a metric used in binary classification tasks, combining both precision and recall into a single measure. It's calculated as the harmonic mean of precision and recall. Here's the formula:

                 <img style='width:200px;height:auto;' src='https://res.cloudinary.com/dpg6ubeyo/image/upload/v1715169187/f1_score_k0cie7.png' />

                Precision measures the accuracy of positive predictions, while recall measures the ability of the model to correctly identify positive instances. The F1 Score provides a balance between precision and recall, making it a useful metric when dealing with imbalanced datasets or when both false positives and false negatives are important. It ranges from 0 to 1, where 1 indicates perfect precision and recall, while 0 indicates the worst performance.
                </p>
                <span style='font-weight:bold;'>0.48611369990680336</span>
                </div>
                ''',unsafe_allow_html=True)
    line_add()
    st.write('')
    st.markdown('''
                <div style="margin:10px;padding:10px;">
                <h3>Confusion Matrix</h3>
                <p>
                Confusion Matrix, is a metric used to evaluate the performance of a classification model. It particularly compares the actual and predicted classes to assess how well the model performs.

                A confusion matrix displays four different outcome categories:

                - **True Positives (TP)**: Instances where the model correctly predicts the positive class.
                - **False Positives (FP)**: Instances where the model incorrectly predicts the positive class.
                - **True Negatives (TN)**: Instances where the model correctly predicts the negative class.
                - **False Negatives (FN)**: Instances where the model incorrectly predicts the negative class.

                These four categories can be used to analyze the performance of the classification model in more detail. Performance metrics such as precision and recall can be calculated from the confusion matrix.

                The confusion matrix is a valuable tool to understand how accurately the model predicts each class and which classes it confuses. Therefore, it is commonly used to evaluate the performance of classification models and to understand error types.
                </p>
                <img style='width:auto;height:auto;' src='https://res.cloudinary.com/dpg6ubeyo/image/upload/v1715168436/visualization_galv2p.png' />
                </div>
                ''',unsafe_allow_html=True)
    line_add()
    st.write('')
    st.markdown('''
                <div style="margin:10px;padding:10px;">
                <h3>Decision Tree ROC Curve</h3>
                <p>ROC (Receiver Operating Characteristic) Curve is a graphical representation of the performance of a binary classification model, such as a decision tree classifier, across different threshold values. However, decision trees are not typically evaluated using ROC curves, as ROC curves are more commonly associated with models that output probabilities (e.g., logistic regression or support vector machines).

                Decision trees are evaluated using other metrics such as accuracy, precision, recall, F1 Score, and confusion matrix. These metrics provide insights into the performance of the decision tree model in terms of correctly classified instances, true positives, false positives, true negatives, and false negatives.

                If you're interested in evaluating the performance of a decision tree classifier, you can calculate these metrics directly from the predictions of the model on a test dataset without necessarily needing an ROC curve. However, if you're working with an algorithm that provides probability estimates (e.g., a decision tree ensemble method like Random Forest), then you can compute an ROC curve to assess its performance.
                </p>
                
                <img style='width:auto;height:auto;' src='https://res.cloudinary.com/dpg6ubeyo/image/upload/v1715168596/decision_tree_roc_curve_src7ee.png' />
                </div>
                ''',unsafe_allow_html=True)
    line_add()
    st.write('')
    






def line_add():
    st.markdown("""<hr style="border: 0;
                              height: 1px;
                              background: #333;
                              background-image: linear-gradient(to right, #ccc, #333, #ccc);" /> 
                """, unsafe_allow_html=True)