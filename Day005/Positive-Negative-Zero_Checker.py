# Task: Number Sign Checker
# Objective: Correctly identify Zero, Positive, and Negative numbers

num = int(input("Enter Your Number : "))
if (num == 0):
    print("This is a Zero : ", num)
elif (num > 0):
    print("This Positive Number : ",num)
else:
    print("This a Negative Number : ",num)