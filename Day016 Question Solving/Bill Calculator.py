# Purpose: This script automates the billing process for a service-based retail shop.
# Logic: Uses functional programming to process user inputs and calculate total costs.

service_name = input("What you service went: ")
price = int(input(f"Enter price of {service_name}: "))
quantity = int(input("Quantity: "))

# Function definition
def generate_bill(service_name, price, quantity):
    Total_bill =  price * quantity # Logic: Price * Quantity
    print(f"Your Service are {service_name} and Total Bill = {Total_bill} .")


# Function call
generate_bill(service_name, price, quantity)
