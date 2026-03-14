# Task: Greatest of Three Numbers

a = int(input("Enter Your First Number : "))
b = int(input("Enter Your Second Number : "))
c =  int(input("Enter Your Third Number : "))
if (a > b and a > c):
    print(f"{a} is the greatest of Three")
elif (b > c):
    print(f"{b} is the greatest of Three")
else:
    print(f"{c} is the greatest of Three")