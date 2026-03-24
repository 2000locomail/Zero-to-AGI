print("Fuel Price $2/L")
allowed_vehicles = ["Car", "Bike", "Truck"]
while True:
    user = input("Enter User Name: ")
    vehicle_type = input("Enter vehicle type Car/Bike/Truck ?: ").strip().capitalize()
# Validate if the entered vehicle is in the allowed list
    
    if vehicle_type not in allowed_vehicles:
        print("⚠️ Invalid Vehicle Type! We are handle only Bikes, Cars and Trucks .")
        Exit = input("You want Exit Yes/No: ").strip().capitalize()
        if Exit == "Yes":
            break
        else:
            continue
    quantity = float(input("Enter Quantity in Liter: "))

    price = 100*quantity
# --- BIKE LOGIC ---
    if vehicle_type == "Bike":
        if quantity <= 10:
            print(f"{quantity}L Fueling......")
            if price > 1000:
                d_price = price - 200
                print(f"🎁 Special Discount of ₹200 applied! Now total price is {d_price}.")
            else:
                print(f"Total Price is = {price}")
                break
        else:
            print(f"Fuel Limit\nBike: Max 10 Liters")
            continue
# --- CAR LOGIC ---
    elif vehicle_type == "Car":
        if quantity <= 50:
            print(f"{quantity}L Fueling......")
            if price > 1000:
                d_price = price - 200
                print(f"🎁 Special Discount of ₹200 applied! Now total price is {d_price}.")
            else:
                print(f"Total Price is = {price}")
                break
        else:
            print(f"Fuel Limit\nCar: Max 50 Liters")
            continue  
# --- TRUCK LOGIC ---
    elif vehicle_type == "Truck":
        if quantity <= 100:
            print(f"{quantity}L Fueling......")
            if price > 1000:
                d_price = price - 200
                print(f"🎁 Special Discount of ₹200 applied! Now total price is {d_price}.")
            else:
                print(f"Total Price is = {price}")
                break
        else:
            print(f"Fuel Limit\nTruck: Max 100 Liters")
            break