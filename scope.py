WEIGHT_CONVERSION = 0.453592  # 1 pound = 0.453592 kg
HEIGHT_CONVERSION = 0.0254    # 1 inch = 0.0254 meters
def calculate_bmi(weight_lb, height_in):
    weight_kg = weight_lb * WEIGHT_CONVERSION
    height_m = height_in * HEIGHT_CONVERSION
    bmi = weight_kg / (height_m ** 2)
    return bmi
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"
def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the {category} category.")
main()