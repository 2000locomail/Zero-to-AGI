# LEVEL 1: BASIC VARIABLES & MATH OPERATORS
# Task: "The Life Seconds Calculator"
name = input("Enter your name: ")
age = int(input("Enter your age(in years): "))
age_in_sec = age*365*24*60*60 
print(f"Hey {name}, you have spent {age_in_sec} seconds on Earth!")
# ---------------------------------------------------------
# LEVEL 2: CONDITIONALS (if-elif-else)
# Task: "The Smart ATM Simulator"

balance = 5000
amount = int(input("Enter amount you want to withdraw: "))
if amount > balance:
    print(f"Insufficient Funds! Your available balance is {balance}")
elif amount <= 0:
    print("Invalid Amount!")
elif amount <=balance:
    now_bal = balance - amount
    print(f"Transaction Successful! New Balance {now_bal}")
    if now_bal < 1000:
        print(f"Warning you available balance is {now_bal}")

# --------------------------------------------------------
# LEVEL 3: LOOPS (for & while)
# Task: "The Multiplier & Sum Tracker"

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

total_sum = 0
i = 1
while i <= num:
    total_sum += i
    i += 1
print("total sum =", total_sum)

