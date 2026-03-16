# Task: Smart Salary Manager
# Objective: Calculate 20% bonus for experienced employees and show integer division

salary = int(input("Enter Your Salary : "))
experience = int(input("Enter years of Experience : "))
if (experience > 5):
    bonus = salary*1.20
    print(f"Congratulations! Your New Total Salary is: {bonus:.2f}")
    print(f"Salary Multiple (Integer Division): {int(bonus//salary)}")
else:
    print(f"Sorry, no bonus for experience <= 5 years. Your Salary is: {salary}")
