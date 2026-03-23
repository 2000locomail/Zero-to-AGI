# Task: Simple Calculator

num1 = int(input("Enter Your First Number : "))
num2 = int(input("Enter Your Second Number : "))
oper = input("Enter Your Operator Number : ")
if (oper == "*"):
    print("Result is : ", num1*num2)
elif (oper == "-"):
    print("Result is : ", num1-num2)
elif (oper == "+"):
    print("Result is : ", num1+num2)
elif (oper == "/"):
    print("Result is : ", num1/num2)
else:
    print("This a invalid")
