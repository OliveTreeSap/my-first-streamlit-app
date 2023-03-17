import streamlit as st
import sklearn
import pickle
model = pickle.load(open('model.pickle', 'rb'))

st.title("Revenue Prediction")
temp = st.number_input('Input Temperature')
if st.button("Predict"):
    revenue = model.predict(temp)
    st.success(revenue)
