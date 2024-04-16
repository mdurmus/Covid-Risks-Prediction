import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.home import home_body
from app_pages.page2 import page2_body


app = MultiPage(app_name="Corona Risk Prediction")

app.app_page("Home Page", home_body)
app.app_page("Page 2", page2_body)

app.run()