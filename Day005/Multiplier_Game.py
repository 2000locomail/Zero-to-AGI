# Task: The Multiplier Game
# Objective: Conditionally repeat a string based on an integer input

string = input("Enter any Word : ")
num = int(input("Enter a Number : "))
if (num > 5):
    string2_x = string*2
    print(string2_x)
else:
    print(string)