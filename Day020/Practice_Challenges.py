# =========================================================
# DAY 20: STEP-BY-STEP LOOP & RECURSION CHALLENGES
# =========================================================

# ---------------------------------------------------------
# LEVEL 1: BASIC LOOPS (Warm-up)
# ---------------------------------------------------------

# TASK 1: Multiples of 3

n = 3
for i in range (1,11):
    print(i*n)

# TASK 2: Sum of Evens

for y in range (2,51,2):
        print(y, "is even")

total_sum = 0
t = 2
while t <= y:
    total_sum += t
    t += 2
print("total sum =", total_sum)

# LEVEL 2: LOOP LOGIC (Number Games)


# TASK 3: Reverse the Number

num = int(input("Enter a Number you want to reverse: "))
org_num = num
rev = 0
while num > 0:
    last_digit = num % 10
    rev = (rev*10) + last_digit
    num = num // 10
print(f"Reverse of no: {org_num} is = {rev}")

# TASK 4: Prime Checker

n = int(input("Enter a number to check prime: "))

if n < 2:
    print(f"{n} is not a Prime Number.")
else:
    is_prime = True
    for p in range(2,n):
        if n % p == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a Prime Number.")
    else:
        print(f"{n} is not a Prime Number.")
    

