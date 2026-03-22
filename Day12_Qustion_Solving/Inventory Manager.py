items = {
    "Pen" : 10,
    "Car" : 3,
    "Book" : 43,
    "Laptop" : 23,
}
item = input("Enter You have item: ").strip().capitalize()
quantity = int(input("Enter Quantity: "))
if item in items:
    items[item] += quantity
    print(f"Updated {item} quantity to: {items[item]}")
else:
    items[item] = quantity
    print(f"Added new item: {item} with quantity {quantity}")

print("\nFinal Inventory:", items)