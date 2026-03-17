# Task: Smart Electricity Bill Calculator
# Objective: Apply different rates based on unit consumption ranges

unit = int(input("Enter Your Electricity Units: "))
if (unit < 100):
    unitbill5 = unit*5
    print("Your Electricity Bill is: ",unitbill5)
elif(100 <= unit <= 300):
    unitbill7 = unit*7
    print("Your Electricity Bill is: ",unitbill7)
else:
    unitbill10 = unit*10
    print("Your Electricity Bill is: ",unitbill10)