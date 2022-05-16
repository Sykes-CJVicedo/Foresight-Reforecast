from ctypes import cdll
from distutils.command.upload import upload
from queue import Empty
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from prophet import Prophet
from prophet.plot import plot_plotly

#Page Title
st.set_page_config(layout="wide", page_title='Foresight - Reforecast')

#Sidebar - File Upload - Captions
st.sidebar.write('# REFORECAST')
st.sidebar.write(
    'To begin using the app, import your CSV file by simply clicking the "Browse files" button below.')

#Sidebar Upload
maxUploadSize = 1000
uploadedfile = st.sidebar.file_uploader(' ', type=['.csv'])

if uploadedfile is not None:
    uploadedData = pd.read_csv(uploadedfile)
    uploadedData['Year-Month'] = uploadedData['Year'].map(str) +"-" +uploadedData['Month'].map(str)
    uploadedData['ds'] = pd.to_datetime(uploadedData['Date'])
    uploadedData['y'] = np.dtype('int64').type(uploadedData['Actual'])


    #Preview of Data
    st.title('Data Preview')
    PreviewOption = st.selectbox(
        'Select part of the data you want to see',
        ('First 10 Rows','Last 10 Rows'))
    if PreviewOption == "First 10 Rows":
            st.dataframe(uploadedData.head(11))
    elif PreviewOption == "Last 10 Rows":
            st.dataframe(uploadedData.tail(11))
    else:
            st.write("")

    #Current Trend line
    LineData = uploadedData[['Year-Month','Actual','Forecast']].copy()
    fig = px.line(
        LineData,
        x = "Year-Month",
        y = ["Actual","Forecast"]
    )
    st.plotly_chart(fig)

    #Forecast
    forecastData = uploadedData[['ds','y']].copy()


    model = Prophet()
    model.fit(forecastData)
    future = model.make_future_dataframe(periods=100)
    forecast = model.predict(future)

    fig = plot_plotly(model, forecast)
    fig.update_layout(
        title="Reforecast"
    )

    st.plotly_chart(fig)

else:
    st.write('Please Attach your File')
