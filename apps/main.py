import streamlit as st
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
scripts_dir = parent_dir+"/scripts"
data_directory = parent_dir+"/data"

sys.path.insert(1, '../scripts')

from core import MultiApp
import predictor # import your app modules here

app = MultiApp()

st.sidebar.markdown('# **Rossmann Pharmaceuticals Sales Prediction**')
st.sidebar.markdown("""
Random Forest Regression model based sales and number of customers forcaster
""")

# Add all your application here
app.add_app("Model", predictor.app)
# The main app
app.run()