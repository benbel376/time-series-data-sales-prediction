
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import pickle

import sys
sys.path.append("..")
model = pickle.load(open("models/RFR-sales-27-05-2022-09-40-35.pkl", 'rb'))
scaler = pickle.load(open('models/scaler-27-05-2022-09-40-35.pkl', 'rb'))


def app():

    st.title("Predict your sale")
    st.subheader("This model will predict the sales and number of customers on a specified date")
    Store = st.number_input("Store ID", min_value=1, max_value=1115)
    uploaded_file = st.file_uploader("Choose a file")
    dist = st.number_input("Competition Distance", min_value=1, max_value=20000)
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



    calculate = st.button('Calculate')
    if ((uploaded_file is not None) and (calculate)):
        input = pd.read_csv(uploaded_file)
        st.write(input)
        list_data = input.to_dict()
        select_list = ["Month", "WeekOfYear", "DayOfWeek", "DayOfMonth", "Promo","Open"]
        new_dict = {}
        for i in range(len(select_list)):
            new_dict[select_list[i]] = list_data[select_list[i]]

        new_df = pd.DataFrame(new_dict)
        
        st.write(new_dict)
        
        new_df.insert(1, 'Assortment', Assortment)
        new_df.insert(2, 'StoreType', StoreType)
        new_df.insert(7, "Store", Store)
        new_df.insert(8, "CompDist", dist)
        #input_data = minmax_scale(np.array(input_data))
        
        st.write(new_df.head())
        prediction = model.predict(new_df)
        new_df.insert(0, "Sales", prediction)
        rev_sca = scaler.inverse_transform(new_df)
        rev_sca = pd.DataFrame(rev_sca)
        st.write(rev_sca.head())
        st.write("The predicted sale is: {}".format ( rev_sca.loc[0,0]))