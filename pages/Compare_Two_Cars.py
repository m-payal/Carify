import streamlit as str1
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

import matplotlib.pyplot as plt
DATE_TIME = "date/time"
DATA_URL = pd.read_csv("Datasets/SIH.csv",error_bad_lines=False)

str1.set_page_config(page_title="Car Comparison", page_icon="🚗")

str1.subheader("COMPARE TWO CAR")
str1.write("CAR 1")
selectt = str1.selectbox('Company Name', ['Hyundai','Ford','Honda','KIA'],key=4)
if selectt =='Hyundai':
    selectt1 = str1.selectbox('Model Name', ['All New Santro', 'Creta', 'Grand i10','i20'],key=8)
if selectt == 'Ford':
    selectt1 = str1.selectbox('Model Name', ['Ecosports', 'Figo',],key=12)
if selectt == 'Honda':
    selectt1 = str1.selectbox('Model Name', ['Amaze', 'City(2014)', 'WR-V'],key=16)
if selectt == 'KIA':
    selectt1 = str1.selectbox('Model Name', ['Carnival'],key=20)

selectt2 = str1.selectbox('City', ['Mumbai','Delhi','Srinagar','Shimla','Vishakhapattnam'],key=11)
selectt4 = str1.selectbox('Fuel', ['Petrol','1.1 Petrol','1.2L Petrol','1.5L Petrol','Diesel','1.4L Diesel','1.5L Diesel','2.2L Diesel'],key=13)
selectt3 = str1.slider("Age of the vehicle.", 0, 200)

str1.write("CAR 2")
selecttt = str1.selectbox('Company', ['Hyundai', 'Ford', 'Honda', 'KIA'],key=15)
if selecttt == 'Hyundai':
    selecttt1 = str1.selectbox('Model Name.', ['All New Santro', 'Creta', 'Grand i10', 'i20'],key=20)
if selectt == 'Ford':
    selecttt1 = str1.selectbox('Model Name.', ['Ecosports', 'Figo', ],key=21)
if selecttt == 'Honda':
    selecttt1 = str1.selectbox('Model Name.', ['Amaze', 'City(2014)', 'WR-V'],key=22)
if selectt == 'KIA':
    selecttt1 = str1.selectbox('Model Name.', ['Carnival'],key=23)

selecttt2 = str1.selectbox('City', ['Mumbai', 'Delhi', 'Srinagar', 'Shimla', 'Vishakhapattnam'],key=17)
selecttt4 = str1.selectbox('Fuel', ['Petrol','1.1 Petrol','1.2L Petrol','1.5L Petrol','Diesel','1.4L Diesel','1.5L Diesel','2.2L Diesel'],key=18)
selecttt3 = str1.slider("Age of the vehicle", 0, 200)

if str1.button('Compare'):
    str1.write("Comparing.....")
    grouped = DATA_URL.groupby(['Company', 'Model', 'Fuel', 'City'])
    g = grouped.get_group((selectt, selectt1, selectt4, selectt2))
    str1.write(g)

    g1 = grouped.get_group((selecttt, selecttt1, selecttt4, selecttt2))
    str1.write(g1)
