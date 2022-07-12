# BMI Calculator
# Enter weight and height
# Using metrics of kg and cm
Weight = float(input("Enter your weight in kg:"))
Height = float(input("Enter your height in cm:"))
# Formula
bmi = (Weight/Height ** 2) * 10000
print(f"Your BMI is {bmi}")
if bmi <= 18.5:
    print("You are underweight.")
elif bmi <= 18.5 - 24.9:
    print("You are at a normal weight.")
elif bmi <= 25-29.0:
    print("You are over weight.")
elif bmi <= 30:
    print("You are at a obesity weight.")
else:
    print("You are at a severely obese weight.")
if bmi <= 18.5:
    print("Try implementing a healthy diet.")
elif bmi <= 25-29.0:
    print("Try implementing exercise to your routine.")
elif bmi <= 30:
    print("Try implementing a healthy diet and exercise to your routine.")
else:
    print("Contact a primary care physician for further care.")
