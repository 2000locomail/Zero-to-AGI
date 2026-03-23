# Task: Traffic Fine System
# Objective: Categorize traffic violations based on speed ranges

speed = int(input("Enter Speed : "))
if (speed < 60):
    print("No Fine")
elif(speed >= 60 and speed <= 80):
    print("₹500 Fine")
else:
    print("₹2000 Fine + License Suspend")