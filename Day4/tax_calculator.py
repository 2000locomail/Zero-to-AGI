# Task: The Salary Tax Manager
salary = int(input("Enter your Salary: "))

if salary > 100000:
    # 30% Tax 
    final_salary = salary - (salary * 0.30)
    tax = "30%"
elif salary >= 50000:
    # 20% Tax 
    final_salary = salary - (salary * 0.20)
    tax = "20%"
else:
    # 5% Tax 
    final_salary = salary - (salary * 0.05)
    tax = "5%"

print(f"Your tax bracket is {tax}.")
print(f"Your Final Salary after tax deduction is: {final_salary}")