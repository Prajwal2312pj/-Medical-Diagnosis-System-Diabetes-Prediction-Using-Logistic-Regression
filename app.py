import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('diabetes_model.pkl', 'rb'))

# Webpage title
st.title('🧬 Diabetes Prediction Web App')
st.subheader("Enter patient's health info to predict diabetes")

# Input fields
Pregnancies = st.number_input('Pregnancies', min_value=0)
Glucose = st.number_input('Glucose Level', min_value=0)
BloodPressure = st.number_input('Blood Pressure', min_value=0)
SkinThickness = st.number_input('Skin Thickness', min_value=0)
Insulin = st.number_input('Insulin', min_value=0)
BMI = st.number_input('BMI')
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function')
Age = st.number_input('Age', min_value=0)

# Predict button
if st.button('Predict'):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('❌ The person is likely to have Diabetes.')
    else:
        st.success('✅ The person is unlikely to have Diabetes.')
