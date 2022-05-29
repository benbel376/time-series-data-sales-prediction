import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append("..")
model = pickle.load(open("models/RFR-sales-27-05-2022-09-40-35.pkl", 'rb'))
scaler = pickle.load(open('models/scaler-27-05-2022-09-40-35.pkl', 'rb'))

select_list = ["Month", "WeekOfYear", "DayOfWeek", "DayOfMonth", "Promo","Open"]

def plot(df, title):
    plt.figure(figsize=(15, 7))
    sns.set(style="ticks")
    sns.set(font_scale = 2)
    sns.set_style("white")
    sns.set_style("whitegrid")
    sns.despine()
    ax = sns.lineplot(x=df[df.columns[0]], y=df[df.columns[1]])
    ax.spines['left'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    plt.title(title)
    plt.savefig("temp_image.png")
    st.image("temp_image.png")

def app():

    st.title("Predict your sale")
    st.subheader("This model will predict the sales and number of customers on a specified date")
    Store = st.number_input("Store ID", min_value=1, max_value=1115)
    st.markdown("<p style='color: red'><em>Please, make sure your dataset has the structure defined in the Rossman page</em></p>", unsafe_allow_html=True)
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
        new_df = input[select_list]
        new_df.insert(1, 'Assortment', Assortment)
        new_df.insert(2, 'StoreType', StoreType)
        new_df.insert(7, "Store", Store)
        new_df.insert(8, "CompDist", dist)
        new_df.insert(0, "Sales", 0)
        new_df[:] = scaler.transform(new_df[:])
        new_df.pop("Sales")
        prediction = model.predict(new_df)
        new_df.insert(0, "Sales", prediction)
        
        new_df[:] = scaler.inverse_transform(new_df[:])
        
        st.subheader("The calculated sales:")
        st.write(new_df)
        
        aggr_m = new_df[["Month", "Sales"]].groupby(["Month"]).agg({"Sales": "mean"}).reset_index()
        aggr_w = new_df[["WeekOfYear", "Sales"]].groupby(["WeekOfYear"]).agg({"Sales": "mean"}).reset_index()
        aggr_wd = new_df[["DayOfWeek", "Sales"]].groupby(["DayOfWeek"]).agg({"Sales": "mean"}).reset_index()
        aggr_md = new_df[["DayOfMonth", "Sales"]].groupby(["DayOfMonth"]).agg({"Sales": "mean"}).reset_index()

        plot(aggr_m, "Average Sales Accross Months")
        st.markdown("""---""")
        plot(aggr_w, "Average Sales Across Weeks")
        st.markdown("""---""")
        plot(aggr_wd, "Average Sales Across Days of the Week")
        st.markdown("""---""")
        plot(aggr_md, "Average Sales Across Days of the Month")
       

if __name__ == "main":
    pass