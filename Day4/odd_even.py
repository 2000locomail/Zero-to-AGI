# Task: Odd-Even finder
# 1. Take integer input from the user
number = int(input("Enter Your Number : "))
# 2. Use the ternary operator to check the condition
# If number % 2 is 0, it is 'Even', otherwise it is 'Odd'
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number is : {result}")