import streamlit as st

def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    st.title("BMI Calculator 🏋️‍♂️")
    st.write("Welcome to the BMI Calculator! Enter your weight and height to calculate your BMI.")

    # Input fields for weight and height
    weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=300.0, value=70.0)
    height = st.number_input("Enter your height (in meters):", min_value=0.5, max_value=3.0, value=1.75)

    # Calculate BMI
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        # Display results
        st.success(f"Your BMI is: {bmi:.2f}")
        st.info(f"Category: {category}")

        # Show BMI chart
        st.write("### BMI Categories:")
        st.write("- Underweight: BMI < 18.5")
        st.write("- Normal weight: 18.5 ≤ BMI < 24.9")
        st.write("- Overweight: 25 ≤ BMI < 29.9")
        st.write("- Obesity: BMI ≥ 30")

if __name__ == "__main__":
    main()