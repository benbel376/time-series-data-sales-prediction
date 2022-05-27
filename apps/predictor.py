import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import pickle

import sys
sys.path.insert(1, '../scripts')


def app():

    st.title("Predict your sale")
    st.subheader("This model will predict the sales and number of customers on a specified date")

    model = pickle.load(open("../models/RFR-sales-27-05-2022-09-40-35.pkl", 'rb'))
    scaler = pickle.load(open('../models/scaler-27-05-2022-09-40-35.pkl', 'rb'))
    
    DayOfMonth = 3
    DayOfWeek = 4
    WeekOfYear = 30
    Month = 7
    upload = 2


    upl= st.radio(
    "Do you want to upload the date info",
    ('Enter', 'Upload'))

    if upl == 'Upload':
        upload = 1
    else:
        upload = 0


    with st.form(key='my_form'):
        
        if(upload == 1):
            uploaded_file = st.file_uploader("Choose a file")
            if uploaded_file is not None:
                # Can be used wherever a "file-like" object is accepted:
                dataframe = pd.read_csv(uploaded_file)
                st.write(dataframe)
                DayOfMonth = dataframe.iloc[0,1]
                DayOfWeek = dataframe.iloc[0,2]
                WeekOfYear = dataframe.iloc[0,3]
                Month = dataframe.iloc[0,4]
        elif(upload == 0):
            Month = st.number_input("Month", min_value=1, max_value=12)
            DayOfMonth = st.number_input("Day of Month", min_value=1, max_value=31)
            DayOfWeek = st.number_input("Day of Week", min_value=1, max_value=7)
            WeekOfYear = st.number_input("Week of Year", min_value=1, max_value=52)
            
        

        Open = 0
        status = st.radio(
        "Is the store Open or Closed",
        ('Open', 'Closed'))

        if status == 'Open':
            Open = 1
        else:
            Open = 0

        
        dist = st.number_input("Competition Distance", min_value=1, max_value=20000)
        Store = st.number_input("Store ID", min_value=1, max_value=1115)
        Promo = 0
        PromoS = st.radio(
        "Is there a promotion",
        ('Present', 'Absent'))

        if PromoS == 'Present':
            Promo = 1
        else:
            Promo = 0

        StoreType = 0
        StoreTypes = st.radio(
        "What is the store type",
        ('A', 'B', 'C', 'D'))

        if StoreTypes == 'A':
            StoreType = 0
        elif StoreTypes == 'B':
            StoreType = 1
        elif StoreTypes == 'C':
            StoreType = 2
        else:
            StoreType = 3

        Assortment = 0
        assort = st.radio(
        "What is the assortment of the store",
        ('Basic', 'Extra', 'Extended'))

        if assort == 'Basic':
            Assortment = 0
        elif assort == 'Extra':
            Assortment = 1
        else:
            Assortment = 2

        submit_button = st.form_submit_button(label='Submit')
    
    input_data = [0, Month,Assortment, StoreType, WeekOfYear, DayOfWeek, DayOfMonth, Promo, Store, dist, Open]
    input_keys = ["Sales", "Month", "PromoInterval", "Assortment", "StoreType", "WeekOfYear", "DayOfWeek", "DayOfMonth", "Promo", "Store", "dist","Open"]
    input_dict = {}
    for i in range(len(input_data)):
        input_dict[input_keys[i]] = [input_data[i]]
        
    input_df = pd.DataFrame(input_dict)
    if st.button('Calculate'):
        #input_data = minmax_scale(np.array(input_data))
        
        scaled_df = scaler.transform(input_df)
        scaled_df = scaled_df[:,1:]
        prediction = model.predict(scaled_df)
        scaled_arr2 = pd.DataFrame(scaled_df)
        scaled_arr2.insert(0, 11, prediction[0])
        rev_sca = scaler.inverse_transform(scaled_arr2)
        rev_sca = pd.DataFrame(rev_sca)
        st.write(rev_sca)
        st.write("The predicted sale is: {}".format ( rev_sca.loc[0,0]))