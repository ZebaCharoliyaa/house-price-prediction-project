import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("house_model.pkl")
scaler = joblib.load("scaler.pkl")

# Custom Header
st.markdown(
    """
    <div style='text-align: center'>
        <h1 style='color: #4CAF50;'>🏠 House Price Predictor</h1>
        <p style='font-size: 18px;'>Estimate property prices based on key features like size, quality, and year built.</p>
    </div>
    <hr style='margin-top: 0px;'>
    """,
    unsafe_allow_html=True
)

# Input form in two columns
col1, col2 = st.columns(2)

with col1:
    overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    garage_cars = st.slider("Garage Cars", 0, 4, 2)
    full_bath = st.slider("Full Bathrooms", 0, 4, 2)

with col2:
    gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", 500, 5000, 1500)
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
    year_built = st.slider("Year Built", 1900, 2023, 2000)

# Predict button
if st.button("Predict House Price"):
    features = np.array([[overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, full_bath, year_built]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.0f}")

# Footer
st.markdown(
    "<hr><center><small>Developed by Zeba | Machine Learning Project</small></center>",
    unsafe_allow_html=True
)
