# Task: Triangle Validity Checker
# Objective: Verify if three angles form a valid triangle (Sum must be exactly 180 degrees)

ang1 = int(input("Enter Triangle First angle : "))
ang2 = int(input("Enter Triangle Second angle : "))
ang3 = int(input("Enter Triangle Third angle : "))
if (ang1 + ang2 + ang3 == 180):
    print("Valid Triangle")
else:
    print("Invalid")
