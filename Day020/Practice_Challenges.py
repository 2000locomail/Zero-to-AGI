# =========================================================
# DAY 20: STEP-BY-STEP LOOP & RECURSION CHALLENGES
# =========================================================

# ---------------------------------------------------------
# LEVEL 1: BASIC LOOPS (Warm-up)
# ---------------------------------------------------------
"""
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
        print(f"{n} is not a Prime Number.")"""
    
# LEVEL 3: NESTED LOOPS (Patterns & Grids)


# TASK 5: Square Star Pattern
# User se n = 4 input lo aur ye print karo:
# * * * *
# * * * *
# * * * *
# * * * *


# TASK 6: Inverted Triangle
# User se rows 'n' input lo aur ye pattern print karo:
# * * * *
# * * *
# * *
# *

# ---------------------------------------------------------
# LEVEL 4: RECURSION BASICS (The Self-Call)
# ---------------------------------------------------------

# TASK 7: Factorial via Recursion
# factorial(n) function banao jo 5! = 5*4*3*2*1 calculate kare.


# TASK 8: Recursive Sum
# Ek function 'sum_n(n)' banao jo 1 se n tak ka sum recursion se kare.
# Example: sum_n(5) -> 15

# ---------------------------------------------------------
# LEVEL 5: RECURSION MASTERY (Brain Teasers)
# ---------------------------------------------------------

# TASK 9: Fibonacci nth Term
# Fibonacci sequence (0, 1, 1, 2, 3, 5, 8...) ka n-th number nikalo.
# Hint: fib(n) = fib(n-1) + fib(n-2)


# TASK 10: Sum of Digits (Recursive)
# Ek number lo (e.g., 432) aur recursion se digits ka sum (4+3+2 = 9) nikalo.
