# Task: AI Crypto Locker
# Objective: Extract first and last characters and mask the middle

string = input("Enter Your Secret Password: ").strip()
first_char = string[0]
last_char = string[-1]
encrypted = first_char+"X"+last_char
print("Original Data:", string)
print("Encrypted Version:", encrypted)