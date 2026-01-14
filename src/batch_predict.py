import pandas as pd
from predictor import predict_customer
def batch_predict(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    required_cols = {"Age", "Income", "AgeGroup"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required_cols}")

    probabilities = []
    decisions = []
    interpretations = []

    for _, row in df.iterrows():
        prob, decision, interpretation = predict_customer(
            age=row["Age"],
            income=row["Income"],
            age_group=row["AgeGroup"]
        )

        probabilities.append(prob)
        decisions.append(decision)
        interpretations.append(interpretation)

    df["Buy_Probability"] = probabilities
    df["Prediction"] = decisions
    df["Interpretation"] = interpretations

    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    input_csv = "customer.csv"
    output_csv = "customers_with_predictions2.csv"

    batch_predict(input_csv, output_csv)
    print("Batch prediction completed successfully.")    