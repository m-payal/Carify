import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

import matplotlib.pyplot as plt
DATE_TIME = "date/time"
DATA_URL = pd.read_csv("Datasets/SIH.csv",error_bad_lines=False)

fig, ax = plt.subplots()
df=DATA_URL
grouped1=df.groupby(['City'])
height = grouped1['Total cost'].sum()
st.write("COST vs CITY")
plt.bar(np.arange(5), height)
plt.xticks(np.arange(5), ('Mumbai','Delhi','Srinagar','Shimla','Vishakhapattnam'))
plt.xlabel('City')
plt.ylabel('Total cost')
st.plotly_chart(fig)


fig, ax = plt.subplots()
grouped1=df.groupby(['Company'])
height = grouped1['Total cost'].sum()
st.write("COST vs Company")  
plt.bar(np.arange(4), height)
plt.xticks(np.arange(4), ('Hyundai','Ford','Honda','KIA'))
plt.xlabel('Company')
plt.ylabel('Total cost')
st.plotly_chart(fig)
