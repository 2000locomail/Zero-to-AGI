# Project: Tvarnip Inventory & Billing Engine
# Objective: Check stock, calculate bill, and update dictionary

inventory = {
    "Apple": {"price": 100, "stock": 20},
    "Banana": {"price": 50, "stock": 50},
    "Mango": {"price": 200, "stock": 15}
}

item_name = input("Enter Product Name: ").strip().capitalize()

product_info = inventory.get(item_name, "Not in Stock")

if product_info != "Not in Stock":
    print(f"Available Stock for {item_name}: {product_info['stock']}")
    
    qty = int(input(f"How many {item_name} do you want? "))
    
    if product_info['stock'] >= qty:
        
        total_bill = qty * product_info['price']
        
        
        inventory[item_name]['stock'] -= qty
        
        print(f"\n--- Order Successful ---")
        print(f"Total Bill: ₹{total_bill}")
        print(f"Updated Stock for {item_name}: {inventory[item_name]['stock']}")
    else:
        print(f"\nError: Limited stock! Only {product_info['stock']} available.")
else:
    print(f"\nStatus: {product_info} ")