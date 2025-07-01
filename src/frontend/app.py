import streamlit as st
import requests

st.title("🌼 Iris Classifier (MLOps Pipeline)")

features = []
for i in range(4):
    value = st.slider(f"Feature {i+1}", 0.0, 10.0, step=0.1)
    features.append(value)

if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict", json={"features": features})
    if response.status_code == 200:
        st.success(f"Prediction: {response.json()['prediction']}")
    else:
        st.error("Failed to get prediction")