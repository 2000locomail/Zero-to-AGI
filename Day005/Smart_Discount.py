# Task: Optimized Smart Discount Store
# Objective: Apply discounts efficiently by calculating only when conditions are met.

amount = int(input("Enter Your billing amount : "))
if (amount >= 2000 and amount <= 5000):
    dis10 = amount-(amount*0.1)
    print(f"10% discount applied! You will pay : {dis10:.2f}")
elif (amount > 5000):
    dis15 = amount-(amount*0.15)
    print(f"15% discount applied! You will pay : {dis15:.2f}")
else:
    print(f"0% discount. You will pay : {amount}")