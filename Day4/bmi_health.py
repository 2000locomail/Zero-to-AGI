# Task: BMI Calculator 

weight = int(input("Enter Your Weight in (Kg) : "))
height = float(input("Enter Your Height in (m) : "))
BMI = weight / (height**2)
if (BMI < 18.5):
    print(f"You Underweight and your BMI is : {BMI:.2f}")
elif (BMI <= 24.9):
    print(f"You Normal and your BMI is : {BMI:.2f}")
elif (BMI <= 29.9):
    print(f"You Overweight and your BMI is : {BMI:.2f}")
else:
    print(f"You Obese and your BMI is : {BMI:.2f}")
