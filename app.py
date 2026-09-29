import streamlit as st
import requests

st.title("📊 Student Score Predictor")

hours = st.slider("Hours Studied", 0.0, 10.0, 5.0, 0.5)

if st.button("Predict Score"):
    response = requests.post("http://127.0.0.1:8000/predict-score/", json={"hours_studied": hours})
    if response.status_code == 200:
        st.success(f"🎯 Predicted Score: {response.json()['predicted_score']}")
    else:
        st.error("Prediction failed.")