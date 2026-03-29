# Authenticate users and manage their balance (Check, Add, Withdraw)

vault = {"Gadu": 1000, "Jeax": 5000}
name = input("Enter Your Name: ").strip()
# Check user identity

if name in vault:
    print(f"Access Granted! Welcome {name} .")
    i = 0
    # Process services for a limited number of attempts
    while i < 1:
        service = input("Choose service: \n1. Check Balance \n2. Add Money \n3. Withdraw Money \n4.Exit \n Choose: ")

        # Display current balance
        if service == "Check Balance":
            print(vault[name],"rs.")
        # Add funds to vault
        elif service == "Add Money":
            amount = int(input("Enter Amount: "))
            vault[name] += amount
            print(f"Now Your Balance is {vault[name]} rs.")
        # Withdraw funds 
        elif service == "Withdraw Money":
            amount = int(input("Enter Amount: "))
            if amount <= vault[name]:
                vault[name] -= amount
                print(f"Now Your Balance is {vault[name]} rs.")
            else:
                print(f"You don't have {amount} rs.! Try again.")
        # Manually exit the service
        elif service == "Exit":
            break
        i += 1 # Increment attempt counter
else:
    print("Access Denied! Name not found, Try again.")




