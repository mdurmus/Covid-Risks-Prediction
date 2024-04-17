import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.home import home_body
from app_pages.dataset import dataset_body

st.set_page_config(
    page_title="Corona Risk Prediction",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="auto"
)

app = MultiPage(app_name="Corona Risk Prediction")

app.app_page("Home Page", home_body)
app.app_page("Dataset", dataset_body)

menu_bg_image='''
<style>
[data-testid="stSidebar"] > div:first-child {
background-image: url("https://as1.ftcdn.net/v2/jpg/04/32/38/52/1000_F_432385234_scY4zKgKV6JXfWzyZfLq210CRMrt246k.jpg");
}

section.main{
background-color:#f0f8ff;
}
div.stHeadingContainer{
    display:none;
}

div.st-emotion-cache-cnbvxy.e1nzilvr5{
    color:#004085;
    border-color:red;
}

[data-testid="stTableStyledTable"] {
  color: #000;
  border: 3px solid blue;
  border-collapse: collapse;
  width:100%;
}

[data-testid="stTableStyledTable"] th, 
[data-testid="stTableStyledTable"] td {
  border: 1px solid black;
  padding: 8px;
  text-align: left;
}

th.col_heading {
  color: blue;
}

h1{color:red;font-size:30px;line-height:32px;}
h2{color:blue;font-size:28px;line-height:30px;}
h3{color:orange;font-size:24px;line-height:26px;}
</style>
'''
st.markdown(menu_bg_image, unsafe_allow_html=True)
app.run()
