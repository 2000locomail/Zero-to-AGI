# Task: Safe Division Checker
# Objective: Prevent system crash by checking if the denominator is zero

num1 = int(input("Enter your First Number : "))
num2 = int(input("Enter your Second Number : "))
result = num1 / num2
if (num2 == 0):
    print("Division by zero not possible")
else:
    print(f"The Division of {num1} and {num2} is : {result:.2f}")