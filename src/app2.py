import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Load model bundle
# -------------------------------
model_bundle = joblib.load("final_logistic_model.pkl")
model = model_bundle["model"]
threshold = model_bundle["threshold"]

# -------------------------------
# App UI
# -------------------------------
st.set_page_config(page_title="Customer Purchase Predictor", layout="centered")

st.title("🛒 Customer Purchase Prediction")
st.write("Fill in customer details to predict purchase likelihood.")

# -------------------------------
# User Inputs
# -------------------------------
age = st.slider("Age", min_value=18, max_value=70, value=35)
income = st.number_input("Monthly Income", min_value=0.0, value=50000.0)
age_group = st.selectbox("Age Group", ["Young", "Middle", "Old"])

# -------------------------------
# Create input DataFrame
# -------------------------------
input_df = pd.DataFrame([{
    "Age": age,
    "Income": income,
    "AgeGroup": age_group
}])

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    probability = model.predict_proba(input_df)[0, 1]
    prediction = int(probability >= threshold)

    st.subheader("Prediction Result")

    st.write(f"**Probability of Purchase:** {probability:.2f}")

    if prediction == 1:
        st.success("✅ Customer is likely to BUY")
    else:
        st.error("❌ Customer is NOT likely to buy")