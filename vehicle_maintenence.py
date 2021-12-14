import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

import matplotlib.pyplot as plt
DATE_TIME = "date/time"
DATA_URL = pd.read_csv("Datasets/SIH.csv",error_bad_lines=False)

st.title("CARIFY - VEHICLE MAINTENENCE")
st.markdown("WELCOME TO CARIFY 💥")
st.write("          HOME")

from PIL import Image
img=Image.open('Images/toyota.jpeg')
st.image(img, width=445)
image = Image.open('Images/mghector.jpeg')
st.image(image, width=445)
##st.write(DATA_URL,width=1000,height=1000)

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import math
from socket import socket
from pandas import DataFrame

# --------------------------------------- KNOW information about your CAR ---------------------------------------------------
if st.sidebar.checkbox("KNOW information about your CAR.", False):
    st.sidebar.subheader("INFORMATION ABOUT YOUR CAR")
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

    # ----------------------------------- PROBABILITY ------------------------------------------------
    import numpy as np
    import scipy.stats
    import pandas as pd
    import matplotlib
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



        from sklearn.metrics import accuracy_score
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.naive_bayes import GaussianNB
        from sklearn.model_selection import train_test_split
        import math
    #-----------------------------------------------------------------------------------
        df=g

        X1 = df.iloc[:, 4:23].values
        y1 = df.iloc[:, 23].values
        df.head()
        X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.24, random_state=42)
        from sklearn.naive_bayes import GaussianNB as gnb

        ### create classifier
        clf = gnb()
        ### fit the classifier on the training features and labels
        clf.fit(X1_train, y1_train)
        y1_predict = clf.predict(X1_test)
        predictions3 = [np.round(value) for value in y1_predict]
        accuracy = accuracy_score(y1_test, predictions3)
        st.write("Drain washer Accuracy: %.2f%%" % (accuracy * 100.0))

        #**************************************

        X1 = df.iloc[:, 4:22].values
        y1 = df.iloc[:, 22].values
        df.head()
        X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.24, random_state=42)
        from sklearn.naive_bayes import GaussianNB as gnb

        ### create classifier
        clf = gnb()
        ### fit the classifier on the training features and labels
        clf.fit(X1_train, y1_train)
        y1_predict = clf.predict(X1_test)
        predictions3 = [np.round(value) for value in y1_predict]
        accuracy = accuracy_score(y1_test, predictions3)
        st.write("Transmission fluid Accuracy: %.2f%%" % (accuracy * 100.0))

        #***************************************

        X1 = df.iloc[:, 4:15].values
        y1 = df.iloc[:, 15].values
        df.head()
        X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.30, random_state=42)
        from sklearn.naive_bayes import GaussianNB as gnb

        ### create classifier
        clf = gnb()
        ### fit the classifier on the training features and labels
        clf.fit(X1_train, y1_train)
        y1_predict = clf.predict(X1_test)
        predictions3 = [np.round(value) for value in y1_predict]
        accuracy = accuracy_score(y1_test, predictions3)
        st.write("spark plug Accuracy: %.2f%%" % (accuracy * 100.0))

        #****************************************

        X1 = df.iloc[:, 4:26].values
        y1 = df.iloc[:, 25].values
        df.head()
        X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.25, random_state=42)
        from sklearn.naive_bayes import GaussianNB as gnb

        ### create classifier
        clf = gnb()
        ### fit the classifier on the training features and labels
        clf.fit(X1_train, y1_train)
        y1_predict = clf.predict(X1_test)
        predictions3 = [np.round(value) for value in y1_predict]
        accuracy = accuracy_score(y1_test, predictions3)
        st.write("part cost Accuracy: %.2f%%" % (accuracy * 100.0))

        #------------------------------------------------------------------------------------------
        import matplotlib.pyplot as plt
        fig = plt.figure()
        left=df["Mileage"]
        height=df["Total cost"]
        #tick_label=['Mumbai','Delhi','Vishakhapattanam','Srinagar']
        plt.scatter(left,height, color=['orange'])
        plt.xlabel('Mileage')
        plt.ylabel('Total cost')

        st.plotly_chart(fig)
 # -------------------------------- COMPARISON ----------------------------------------------------------
if st.sidebar.checkbox("COMPARE TWO CARS?", False):
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
 # ------------------------------- VISUALISATION -----------------------------------------------------------
if st.sidebar.checkbox("VISUALIZATION", False):

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    df=DATA_URL
    left = df["City"]
    height = df["Total cost"]
    st.write("COST vs CITY")
    tick_label=['Mumbai','Delhi','Vishakhapattanam','Srinagar']
    ax.set_xticklabels(tick_label)    
    plt.scatter(left, height, color=['orange'])
    plt.xlabel('City')
    plt.ylabel('Total cost')
    st.plotly_chart(fig)



    left = df["Company"]
    height = DATA_URL.groupby(['Company']).['Total cost'].sum()
    st.write("COST vs Company")
    tick_label=['Hyundai','Ford','Honda','KIA']
    ax.set_xticklabels(tick_label)    
    plt.bar(left, height, color=['blue'])
    plt.xlabel('Companu')
    plt.ylabel('Total cost')
    st.plotly_chart(fig)

 # ------------------------------- ABOUT US -----------------------------------------------------------

if st.sidebar.checkbox("ABOUT US", False):
    st.subheader("ABOUT CARIFY")
    st.write("In Today’s world with so many cars, models in the market, it is hard to find out which car has a high maintenance cost/index that is authentic source.While buying a car we spend a lot of time different features and also maintenance. But there's no platform which tells us the maintenance cost that we'll have to pay after buying the car. A system that shows the health and Maintenance Index of various components of car models or car parts based on multiple factors is needed. We have created this platform for all these problems")
    st.write("In our system we show the health and maintenance Index of various components of car models or car parts based on multiple factors.Also the probablity of replacement of a particular car component after the car is bought. We can also compare two different car models based on maintenence.This will help new buyers to understand the maintenance costs of a certain model and probability of which car part requires more often servicing /change, OEM’s to understand which part is requiring frequent change so they can improve that component and needs to be recalled and made better in the new models ")
    st.subheader('"Know your car\'s life before you buy it!"')
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text(" \n BY TEAM \n Akshata Jedhe \n Juee Ashtaputre \n Payal Mehta \n Riya Kulkarni \n Shreya Pawaskar")
