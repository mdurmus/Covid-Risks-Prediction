import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.home import home_body
from app_pages.page2 import page2_body

st.set_page_config(
    page_title="Corona Risk Prediction",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="auto"
)

app = MultiPage(app_name="Corona Risk Prediction")

app.app_page("Home Page", home_body)
app.app_page("Page 2", page2_body)

menu_bg_image='''
<style>
[data-testid="stSidebar"] > div:first-child {
background-image: url("https://as1.ftcdn.net/v2/jpg/04/32/38/52/1000_F_432385234_scY4zKgKV6JXfWzyZfLq210CRMrt246k.jpg");
}
</style>
'''
st.markdown(menu_bg_image, unsafe_allow_html=True)
app.run()
