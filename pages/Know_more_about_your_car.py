import streamlit as st
import time
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib
   
st.set_page_config(page_title="Your Car Information", page_icon="📈")

st.header("Get to know more about your car's life by simply filling few details")
st.subheader("Please fill in the details")
select = st.selectbox('Company', ['Hyundai','Ford','Honda','KIA'])
if select =='Hyundai':
    select1 = st.selectbox('Model', ['All New Santro', 'Creta', 'Grand i10','i20'])
if select == 'Ford':
    select1 = st.selectbox('Model', ['Ecosports', 'Figo',])
if select == 'Honda':
    select1 = st.selectbox('Model', ['Amaze', 'City(2014)', 'WR-V'])
if select == 'KIA':
    select1 = st.selectbox('Model', ['Carnival'])

select2 = st.selectbox('City', ['Mumbai','Delhi','Srinagar','Shimla','Vishakhapattnam'])
select4 = st.selectbox('Fuel', ['Petrol','1.1 Petrol','1.2L Petrol','1.5L Petrol','Diesel','1.4L Diesel','1.5L Diesel','2.2L Diesel'])
select3 = st.text_input('Enter Age of Vehicle here:')
st.write("Check show data to get the information.")
    
st.text("\n")
if st.checkbox("Show data", False):
    #st.write(DATA_URL.columns)
    grouped=DATA_URL.groupby(['Company','Model','Fuel','City'])
    g=grouped.get_group((select,select1,select4,select2))
    st.write(g)

    from sklearn.model_selection import train_test_split
    d=g.loc[g["Age of Vehicle"] == select3]
    if(d['AC Dust Filter'].values == [0]):
           st.write("Probability of getting AC Dust Filter changed")
           st.write(0, "%")
    else:
        st.write("Probability of getting AC Dust Filter changed")
        st.write(100, "%")
    if(d['Engine oil'].values == [0]):
           st.write("Probability of getting Engine oil changed")
           st.write(0, "%")
    else:
        st.write("Probability of getting Engine oil changed")
        st.write(100, "%")
    if(d['Air cleaner filter'].values == [0]):
           st.write("Probability of getting Air cleaner filter changed")
           st.write(0, "%")
    else:
        st.write("Probability of getting Air cleaner filter changed")
        st.write(100, "%")
