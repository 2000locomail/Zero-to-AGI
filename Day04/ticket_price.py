# Task: Ticket Booking
# Objective: Apply discounts based on age and gender using conditional logic
gender = input("Enter Your Gender M/F/Other : ").upper()
age = int(input("Enter Your Age : "))
if (age <= 5):
    print("Free")
elif (age > 5 and gender == "F"):
    print("50% Discount")
else:
    print("Full Price")