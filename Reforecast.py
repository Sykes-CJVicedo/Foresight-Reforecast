from ctypes import cdll
import streamlit as st
from PIL import Image
import pandas as pd

#Page Title
st.set_page_config(layout="wide", page_title='Foresight - Reforecast')

#Sidebar - File Upload - Captions
st.sidebar.write('# REFORECAST')
st.sidebar.write(
    'To begin using the app, import your CSV file by simply clicking the "Browse files" button below.')

#Sidebar Upload
maxUploadSize = 1000
uploadedfile = st.sidebar.file_uploader(' ', type=['.csv'])

