cart = []
total = 0 

no_of_items = int(input("How many items do you want to add? "))
i = 1

while i <= no_of_items:
    item = input(f"\nEnter name for item {i}: ").strip().capitalize()
    price = int(input(f"Enter price of {item}: "))
    
    cart.append({"name": item, "price": price})
    total += price
    i += 1

if len(cart) > 1:
    remove_choice = input("\nDo you want to remove any item? (yes/no): ").lower()
    if remove_choice == "yes":
        remove_name = input("Enter item name to remove: ").strip().capitalize()
        for item_obj in cart:
            if item_obj["name"] == remove_name:
                total -= item_obj["price"]
                cart.remove(item_obj)
                print(f"{remove_name} removed successfully!")
                break
else:
    print("\nOnly 1 item in cart. Skipping 'Remove' option.")

print("\n--- Final Bill ---")
for product in cart:
    print(f"{product['name']}: ${product['price']}")

if total > 1000:
    discount = total * 0.05
    total -= discount
    print(f"Discount (5%): -${discount}")

print(f"Total Amount to Pay: ${total}")