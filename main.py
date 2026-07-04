#import lib.s
import streamlit as st
import numpy as np
import joblib

# Uploading the model 
model = joblib.load("rf.pkl")
st.title(":::  House Price Prediction  :::")
st.markdown("---")

# input fields for user to enter the features
bedroom = st.number_input("Enter the number of bedroom",min_value=0, value=0)
bathroom = st.number_input("Enter the number of bathroom",min_value=0, value=0)
living_area = st.number_input("Enter the living area ",min_value = 0,value = 2000)
condition_house = st.number_input("Condition of house",min_value=0, value=3)
school = st.number_input("School",min_value=0,value=0)

# Making the prediction
x=[[bedroom,bathroom,living_area,condition_house,school]]
pred = st.button("Predict Price")

# if the predict button is clicked, make the prediction and display the result
if pred==True:
    np_array=np.array(x)
    price=int(model.predict(np_array)[0])
    st.write(f"House price :: {price}")
else:
    st.write("Please click the Predict button to see the result")
