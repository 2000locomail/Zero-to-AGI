# Task: Security Code Validator (Corrected)
# Objective: Check if user input exists in the tuple without list conversion

codes = ("A1", "B2", "C3")
index = input("Enter a number: ").upper().strip()

print("Code") if index in codes else print("Invalid")