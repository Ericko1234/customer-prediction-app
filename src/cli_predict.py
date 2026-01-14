from predictor import predict_customer

def main():
    print("=== Customer Purchase Prediction ===")

    age = int(input("Enter customer's age: "))
    income = float(input("Enter customer's income: "))

    print("\nSelect age group:")
    print("1 - Young")
    print("2 - Middle")
    print("3 - Old")

    choice = input("Enter choice (1/2/3): ")

    age_group_map = {
        "1": "Young",
        "2": "Middle",
        "3": "Old"
    }

    age_group = age_group_map.get(choice)

    if age_group is None:
        print("Invalid age group selection.")
        return

    prob, decision, interpretation, detailed_reasons = predict_customer(age, income, age_group)

    print("\n=== Prediction Result ===")
    print(f"Decision: {decision}")
    print(f"Interpretation: {interpretation}")
    print(f"Probability of buying: {prob:.2%}")
    print(f"Detailed Reasons: {detailed_reasons}")
    

if __name__ == "__main__":
    main()    