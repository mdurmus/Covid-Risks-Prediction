import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.home import home_body
from app_pages.dataset import dataset_body
from app_pages.data import data_body
from app_pages.test import test_body
from app_pages.check import check_body

st.set_page_config(
    page_title="Corona Risk Prediction",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="auto"
)

app = MultiPage(app_name="Corona Risk Prediction")

app.app_page("Project Summary", home_body)
app.app_page("Dataset Features", dataset_body)
app.app_page("Data Features", data_body)
app.app_page("Check Yourself", check_body)
app.app_page("Test Results", test_body)

general_css='''
<style>

[data-testid="stSidebar"] > div:first-child {
background-image: url("https://as1.ftcdn.net/v2/jpg/04/32/38/52/1000_F_432385234_scY4zKgKV6JXfWzyZfLq210CRMrt246k.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
height: 100vh;
margin: 0;
padding: 0;
}

h2{
    color:#0b60b0;
    font-size:32px;
    line-height:36px;
}

h3{
    color:#40a2d8;
    font-size:28px;
    line-height:30px;
}

h4{
    color:#f0edcf;
    font-size:28px;
    line-height:30px;
}

h5{
    color:#ff9bd2;
    font-size:23px;
    line-height:26px;
}

th.col_heading {
  color: #fd951f;
}


</style>
'''
st.markdown(general_css, unsafe_allow_html=True)
app.run()
