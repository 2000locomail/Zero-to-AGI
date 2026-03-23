amount = int(input("Enter amount : "))
balance = 20000
# Condition 1: Must be a multiple of 500 (amount % 500 == 0)
# Condition 2: Must be less than or equal to balance (amount <= balance)
if (amount % 500 == 0) and (amount <= balance):
    print("Withdrawal Successful")
else:
    print("Invalid Amount or Low Balance")
