# Task: The Range Checker
# Objective: Check if a number falls between 10 and 50 (inclusive) using logical 'and'

number = int(input("Enter number : "))
result = number >= 10 and number <= 50
print(f"Is the number between 10 and 50? : {result}")