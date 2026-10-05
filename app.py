import streamlit as st
import pandas as pd
import joblib
model = joblib.load("best_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")
default_input = joblib.load("default_input.pkl")
st.title("Diabetes Readmission Prediction")
st.write("Enter patient details to predict hospital readmission.")
age = st.selectbox(
    "Age",
    ["[0-10)", "[10-20)", "[20-30)", "[30-40)",
     "[40-50)", "[50-60)", "[60-70)", "[70-80)",
     "[80-90)", "[90-100)"]
)
gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)
time_in_hospital = st.number_input(
    "Time in Hospital",
    min_value=1,
    max_value=14,
    value=3
)
num_lab_procedures = st.number_input(
    "Number of Lab Procedures",
    min_value=0,
    max_value=132,
    value=40
)
num_medications = st.number_input(
    "Number of Medications",
    min_value=0,
    max_value=81,
    value=10
)
number_inpatient = st.number_input(
    "Previous Inpatient Visits",
    min_value=0,
    value=0
)
number_emergency = st.number_input(
    "Previous Emergency Visits",
    min_value=0,
    value=0
)
number_outpatient = st.number_input(
    "Previous Outpatient Visits",
    min_value=0,
    value=0
)
if st.button("Predict"):

    input_data = default_input.copy()

    input_data["age"] = age
    input_data["gender"] = gender
    input_data["time_in_hospital"] = time_in_hospital
    input_data["num_lab_procedures"] = num_lab_procedures
    input_data["num_medications"] = num_medications
    input_data["number_inpatient"] = number_inpatient
    input_data["number_emergency"] = number_emergency
    input_data["number_outpatient"] = number_outpatient


    input_processed = preprocessor.transform(input_data)

    
    prediction = model.predict(input_processed)[0]
    class_names = {
        0: "<30",
        1: ">30",
        2: "NO"
    }

    result = class_names.get(int(prediction), str(prediction))
    st.success(f"Predicted Readmission: {result}")
    print(label_encoder.classes_)