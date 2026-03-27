# Calculate data bill with member-only discounts.

members = ("Ramu", "Kalu", "Molu", "Golu", "Dillu")
name = input("Enter your name: ").strip().capitalize()
data_use = float(input(f"Hello {name}! Enter your monthly data use (in GB): "))

# Dynamic Pricing Logic
price_1gb = data_use*10
price_under_5gb = data_use*15
price_more_5gb = data_use*20

# Visual Progress Bar
for percent in range(10, 101, 10):
    print(f"Data Processing... {percent}%")

# Billing and Discount Logic
if data_use <= 1:
    if name in members:
        dicount = price_1gb - price_1gb*0.1
        print(f"Your Data Bill = {price_1gb} rs. You get member-only 10% Discount Your data bill is {dicount} rs.")
    else:
        print(f" Your Data Bill = {price_1gb} rs.")
elif data_use <= 5:
    if name in members:
        dicount = price_under_5gb - price_under_5gb*0.1
        print(f"Your Data Bill = {price_under_5gb} rs. You get member-only 10% Discount Your data bill is {dicount} rs.")
    else:
        print(f"Your Data Bill = {price_under_5gb} rs.")
elif data_use >= 5:
    if name in members:
        dicount = price_more_5gb - price_more_5gb*0.1
        print(f"Your Data Bill = {price_more_5gb} rs. You get member-only 10% Discount Your data bill is {dicount} rs.")
    else:
        print(f" Your Data Bill = {price_more_5gb} rs.")
else:
    print("Invalid!")