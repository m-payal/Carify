import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

import matplotlib.pyplot as plt
DATE_TIME = "date/time"
DATA_URL = pd.read_csv("Datasets/SIH.csv",error_bad_lines=False)


st.subheader("COMPARE TWO CAR")
st.write("CAR 1")
selectt = st.selectbox('Company Name', ['Hyundai','Ford','Honda','KIA'],key=1)
if selectt =='Hyundai':
    selectt1 = st.selectbox('Model Name', ['All New Santro', 'Creta', 'Grand i10','i20'],key=1)
if selectt == 'Ford':
    selectt1 = st.selectbox('Model Name', ['Ecosports', 'Figo',],key=1)
if selectt == 'Honda':
    selectt1 = st.selectbox('Model Name', ['Amaze', 'City(2014)', 'WR-V'],key=1)
if selectt == 'KIA':
    selectt1 = st.selectbox('Model Name', ['Carnival'],key=1)

selectt2 = st.selectbox('City', ['Mumbai','Delhi','Srinagar','Shimla','Vishakhapattnam'],key=1)
selectt4 = st.selectbox('Fuel', ['Petrol','1.1 Petrol','1.2L Petrol','1.5L Petrol','Diesel','1.4L Diesel','1.5L Diesel','2.2L Diesel'],key=1)
selectt3 = st.slider("Age of the vehicle.", 0, 200)

st.write("CAR 2")
selecttt = st.selectbox('Company', ['Hyundai', 'Ford', 'Honda', 'KIA'],key=2)
if selecttt == 'Hyundai':
    selecttt1 = st.selectbox('Model Name.', ['All New Santro', 'Creta', 'Grand i10', 'i20'],key=2)
if selectt == 'Ford':
    selecttt1 = st.selectbox('Model Name.', ['Ecosports', 'Figo', ],key=2)
if selecttt == 'Honda':
    selecttt1 = st.selectbox('Model Name.', ['Amaze', 'City(2014)', 'WR-V'],key=2)
if selectt == 'KIA':
    selecttt1 = st.selectbox('Model Name.', ['Carnival'],key=2)

selecttt2 = st.selectbox('City', ['Mumbai', 'Delhi', 'Srinagar', 'Shimla', 'Vishakhapattnam'],key=2)
selecttt4 = st.selectbox('Fuel', ['Petrol','1.1 Petrol','1.2L Petrol','1.5L Petrol','Diesel','1.4L Diesel','1.5L Diesel','2.2L Diesel'],key=2)
selecttt3 = st.slider("Age of the vehicle", 0, 200)

if st.button('Compare'):
    st.write("Comparing.....")
    grouped = DATA_URL.groupby(['Company', 'Model', 'Fuel', 'City'])
    g = grouped.get_group((selectt, selectt1, selectt4, selectt2))
    st.write(g)

    g1 = grouped.get_group((selecttt, selecttt1, selecttt4, selecttt2))
    st.write(g1)
