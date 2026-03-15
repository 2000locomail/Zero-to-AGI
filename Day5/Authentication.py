# Task: Authentication Shield
# Objective: Secure access by verifying both username and password using logical AND

user = input("Enter Your Username : ")
password = input("Enter Your Password : ")

if (user == "admin" and password == "1234"):
    print("Access Granted")
else:
    print("Intruder Alert")