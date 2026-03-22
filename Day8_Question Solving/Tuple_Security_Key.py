tup = (1, 2, 3, 4, 5, 6, 7, 8)
num = int(input("Enter Any Number: "))
if num in tup:
    position = tup.index(num)
    print(f"Access Granted! ✅ Key found at index: {position}")
else:
    print("Access Denied ❌: Number not in system.")