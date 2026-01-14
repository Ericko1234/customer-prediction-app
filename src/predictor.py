import joblib
import pandas as pd

# Load model bundle
import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "final_logistic_model.pkl")

bundle = joblib.load(MODEL_PATH)

model = bundle["model"]
threshold = bundle["threshold"]


def interpret_probability(prob):
    """
    Convert a probability into a human-readable message.
    """
    if prob < 0.20:
        return "Very low likelihood of purchase"
    elif prob < 0.40:
        return "Low likelihood of purchase"
    elif prob < 0.60:
        return "Moderate likelihood of purchase"
    elif prob < 0.80:
        return "High likelihood of purchase"
    else:
        return "Very high likelihood of purchase"


# Conceptual adding detailed explanation to the code for human understanding
def explain_prediction(prob, age, income):
    reasons = []

    if income > 100000:
        reasons.append("High income increased likelihood")

    if age < 35:
        reasons.append("Younger age increased likelihood")

    if prob < 0.4:
        reasons.append("Overall risk factors outweighed positive signals")

    return reasons    


# Predict function
def predict_customer(age, income, age_group):
    """
    Predict whether a customer will buy.

    Parameters:
    - age (int)
    - income (float)
    - age_group (str): 'Young', 'Middle', or 'Old'

    Returns:
    - probability (float)
    - decision (str)
    """

    # ---- Feature engineering (MUST match training) ----
    data = pd.DataFrame([{
        "Age": age,
        "Income": income,
        "AgeGroup": age_group,
        "Income_Age_Ratio": income / age,
        "AgeSquared": age ** 2,
        "IncomeSquared": income ** 2,
        "Interaction": age * income
    }])

    # ---- Predict probability ----
    prob = model.predict_proba(data)[0, 1]
    # ---- Apply business threshold ----
    decision = "Will Buy" if prob >= threshold else "Will NOT Buy"
    interpretation = interpret_probability(prob)
    detailed_reasons = explain_prediction(prob, age, income)


    return prob, decision, interpretation, detailed_reasons



#sanity check
if __name__ == "__main__":
    prob, decision, interpretation, detailed_reasons = predict_customer(
        age=35,
        income=120000,
        age_group="Middle"
    )
    print(f"Predicted Probability: {prob:.3f}")
    print(f"Decision: {decision}")
    print(f"Interpretation: {interpretation}")
    print(f"Detailed Reasons: {detailed_reasons}")


