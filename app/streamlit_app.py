
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Athena AI - Health Advisor", layout="centered")

# Load model
model = joblib.load("model/risk_predictor_xgb.pkl")

st.title("🤖 Athena AI - Personal Health Risk Advisor")

st.write("Enter your daily health habits and Athena will predict your burnout risk.")

# Collect inputs
age = st.slider("Age", 18, 65, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
sleep_hours = st.slider("Average Sleep per Night (hrs)", 3.0, 10.0, 6.5, 0.5)
screen_time = st.slider("Screen Time (hrs/day)", 0.0, 14.0, 5.0, 0.5)
water_intake = st.slider("Water Intake (liters/day)", 0.0, 5.0, 1.5, 0.1)
meals_skipped = st.slider("Meals Skipped per Week", 0, 14, 3)
stress_level = st.slider("Stress Level (1=Low, 10=High)", 1, 10, 5)
activity_level = st.selectbox("Activity Level", ["Low", "Medium", "High"])
weight_kg = st.number_input("Weight (kg)", 40, 150, 70)
height_cm = st.number_input("Height (cm)", 140, 210, 170)

# Encode input
gender_encoded = 1 if gender == "Male" else 0
activity_map = {"Low": 0, "Medium": 1, "High": 2}
activity_encoded = activity_map[activity_level]

# Assemble features
input_data = pd.DataFrame([[
    age, gender_encoded, sleep_hours, screen_time, water_intake,
    meals_skipped, stress_level, activity_encoded, weight_kg, height_cm
]], columns=[
    "age", "gender", "sleep_hours", "screen_time", "water_intake_liters",
    "meals_skipped_per_week", "stress_level", "activity_level", "weight_kg", "height_cm"
])

# Predict
prediction = model.predict_proba(input_data)[0][1] * 100

# Display result
st.subheader("🧠 Burnout Risk Prediction")
st.metric(label="Burnout Risk", value=f"{prediction:.2f} %")

# Advice section
if prediction >= 70:
    st.error("⚠️ High Risk! Prioritize rest, reduce screen time, and hydrate more.")
elif prediction >= 40:
    st.warning("⚠️ Moderate Risk. Keep an eye on your sleep and stress.")
else:
    st.success("✅ Low Risk. Keep up your healthy habits!")

