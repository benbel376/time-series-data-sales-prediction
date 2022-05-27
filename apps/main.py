import streamlit as st
import sys
sys.path.insert(1, '../scripts')

from multiapp2 import MultiApp
import predictor # import your app modules here

app = MultiApp()

st.sidebar.markdown('# **A/B testing for SmartAd BIO**')
st.sidebar.markdown("""
The repo is all about A/B testing by using two groups the exposed and control group. The exposed group were given the smart ad about brand LUX where as the control groups were given some dummy ad about the brand LUX. Classical and Statistical A/B testing has been used to test. After all the tests our aim is to increase the efficiency of our BIO (Brand Impact Optimization)
""")

# Add all your application here
app.add_app("Model", predictor.app)
# The main app
app.run()