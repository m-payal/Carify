import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Information about your Car", page_icon="📈")

st.sidebar.header("Know more about your car")
st.sidebar.subheader("Please fill in the details")
select = st.sidebar.selectbox('Company', ['Hyundai','Ford','Honda','KIA'])
if select =='Hyundai':
    select1 = st.sidebar.selectbox('Model', ['All New Santro', 'Creta', 'Grand i10','i20'])
if select == 'Ford':
    select1 = st.sidebar.selectbox('Model', ['Ecosports', 'Figo',])
if select == 'Honda':
    select1 = st.sidebar.selectbox('Model', ['Amaze', 'City(2014)', 'WR-V'])
if select == 'KIA':
    select1 = st.sidebar.selectbox('Model', ['Carnival'])

select2 = st.sidebar.selectbox('City', ['Mumbai','Delhi','Srinagar','Shimla','Vishakhapattnam'])
select4 = st.sidebar.selectbox('Fuel', ['Petrol','1.1 Petrol','1.2L Petrol','1.5L Petrol','Diesel','1.4L Diesel','1.5L Diesel','2.2L Diesel'])
select3 = st.sidebar.text_input('Enter Age of Vehicle here:')
st.write("Check show data to get the information.")
    
st.text("\n")

