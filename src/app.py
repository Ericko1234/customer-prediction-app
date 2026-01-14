import streamlit as st
from predictor import predict_customer

st.set_page_config(page_title="Customer Purchase Predictor")

st.title("Customer Purchase Prediction System")
st.markdown("""This tool estimates the likelihood that a customer will make a purchasebased on age and income """)   

st.write(
    "Enter customer details below to predict the likelihood of purchase."
)

age = st.number_input(
    "Customer Age",
    min_value=18,
    max_value=100,
    value=30
)

income = st.number_input(
    "Customer Income",
    min_value=0.0,
    value=50000.0
)

age_group = st.selectbox(
    "Age Group",
    ["Young", "Middle", "Old"]
)



if st.button("Predict"):
    prob, decision, interpretation, detailed_reasons = predict_customer(
        age=age,
        income=income,
        age_group=age_group
    )
    if decision == 1:
        st.success(f"High purchase likelihood ({prob:.0%})")
    else:
        st.warning(f"Low purchase likelihood ({prob:.0%})")

    st.subheader("🔍 Prediction Result")
    st.write(f"**Decision:** {decision}")
    st.write(f"**Confidence:** {interpretation}")
    st.write(f"**Probability:** {prob:.2%}")
    st.subheader("Why this prediction was made")
    st.write(interpretation)

    st.subheader("Key Influencing Factors")
    for reason in detailed_reasons:
        st.write("-", reason)
        
    
           
   
