# Task: E-Commerce Billing Engine
# Objective: Calculate total, apply string-based alerts, and classify customers

item_price = float(input("Enter Item Price: "))
quantity = int(input("Enter Item Quantity: "))
total = item_price*quantity
if (total > 1000):
    print("Discount Applied "*3)

customer_type = "Premium" if total > 1000 else "Regular"
print("Customer Type:", customer_type)

