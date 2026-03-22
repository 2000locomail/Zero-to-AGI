users = {"admin": "1234"}
attempts = 3
while attempts > 0:
    user_name = input("Enter Your User Name: ")
    password = input("Enter Your Password: ")
    find = users.get(user_name)
    if find == password:
        print("Login Success!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid Username or Password, Try again {attempts} attempt is left")
        else:
            print("🚫 System Blocked! Too many failed attempts. Try After Sometimes.")
            
            

