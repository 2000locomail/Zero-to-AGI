# Task: Smart Inventory Counter
# Objective: Correctly count items in a list after batch input

items = []
item1 = input("Enter 1st Item Name: ").lower().strip()
item2 = input("Enter 2nd Item Name: ").lower().strip()
item3 = input("Enter 3rd Item Name: ").lower().strip()
total_items = (item1,item2,item3) # tuple
items.append(total_items)
items.extend(total_items)# tuple to list 
find_item = items.count("milk")
print(f"Total 'milk' items found: {find_item}")
