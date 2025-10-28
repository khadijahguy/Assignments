# Creator: Khady Gueye

""" This is my attendance for January 22, 2025 """

def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

# Take height and weight inputs
try:
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    bmi = calculate_bmi(height, weight)
    print(f"The BMI for this person is {bmi:.2f}.")
except ValueError:
    print("Please enter valid numbers.")
