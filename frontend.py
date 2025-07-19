import streamlit as st 
import requests

API_URL = "http://127.0.0.1:8000/predictor_ml"
st.title("Heart Disease Prediction")
st.markdown('Enter your symptoms below:')

# ✅ These match the FastAPI model
age = st.number_input('Age', min_value=1, max_value=119, value=30)
sex = st.number_input('Sex (0 or 1)', min_value=0, max_value=1, value=0)
cp = st.number_input('Cp', min_value=0, max_value=3, value=0)
trestbps = st.number_input('Trestbps', min_value=80, max_value=200, value=120)
chol = st.number_input('Chol', min_value=100, max_value=400, value=200)
fbd = st.number_input('Fbs', min_value=0, max_value=1, value=0)
restecg = st.number_input('Restecg', min_value=0, max_value=2, value=0)
thalach = st.number_input('Thalach', min_value=60, max_value=250, value=150)
exang = st.number_input('Exang', min_value=0, max_value=1, value=0)
oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=6.0, value=1.0)
slope = st.number_input('Slope', min_value=0, max_value=2, value=1)
ca = st.number_input('Ca', min_value=0, max_value=4, value=0)
thal = st.number_input('Thal', min_value=0, max_value=3, value=1)

if st.button('Predict Heart Patient'):
    input_data = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbd': fbd,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Prediction: {prediction['predicted_category']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
