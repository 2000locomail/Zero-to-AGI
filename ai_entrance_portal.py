special_batch = []

name = input("Enter Your Name : ").capitalize()
age = int(input("Enter Your Age : "))
if (18 <= age <= 25) and name.startswith("S"):
    special_batch.append(name)
    print(f"Welcome {name}, you are added to the: Special Batch")
else:
    print(f"Sorry {name}, you are in the: General Batch")

print("Current Special Batch List:", special_batch)