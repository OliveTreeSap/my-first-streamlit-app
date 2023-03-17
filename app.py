import streamlit as st
import sklearn
import pickle
import numpy as np
model = pickle.load(open('model.pickle', 'rb'))

st.title("Revenue Prediction")
temp = st.number_input('Input Temperature', value=0, step=0)
np.array(temp)
if st.button("Predict"):
    revenue = model.predict(temp.reshape(-1, 1))
    st.success(f"{revenue}")
