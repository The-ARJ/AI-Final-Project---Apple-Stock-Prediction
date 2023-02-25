import streamlit as st
import pandas as pd
import numpy as np
import joblib

#Load the trained model
model = joblib.load('final.joblib')

#Create a simple user interface using Streamlit
st.title('AAPL Stock Price Prediction')

#Get the input data from the user
open_price = st.number_input('Open')
high_price = st.number_input('High')
low_price = st.number_input('Low')

#Create a data array with the input values
data = [[open_price, high_price, low_price, 0, 0, 0]]

#Make a prediction using the trained model
prediction = model.predict(data)

#Show the predicted closing price to the user
st.write('Predicted closing price:', prediction[0])