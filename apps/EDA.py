import streamlit as st
import pandas as pd
import sys

sys.path.append("..")


def app():
    st.markdown("<h1 style='padding:2rem;text-align:left; \
            background-color:orange;color:black;font-size:1.8rem;\
            border-radius:0.2rem;'>Rosmann Pharmaceuticals</h1>", 
            unsafe_allow_html=True)
    st.write("---")
    st.write(
    """
    Rossmann is one of the largest drug store chains in Europe with around 56,200 employees
    and more than 4000 stores. In 2019 Rossmann had more than €10 billion turnover in Germany,
    Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain.

    """
    )

    st.subheader("The dataset")
    st.write(" the dataset should be of the following form:")
    st.write(pd.read_csv("data/sampled_train.csv"))

    st.subheader("Sales trend")
    st.image("charts/sales_day.png")
