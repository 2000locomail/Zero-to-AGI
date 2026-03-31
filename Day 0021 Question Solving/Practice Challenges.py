# ---------------------------------------------------------
# LEVEL 3: NESTED LOOPS (Patterns & Grids)
# ---------------------------------------------------------

# TASK 5: Square Star Pattern
# User se n = 4 input lo aur ye print karo:
# * * * *
# * * * *
# * * * *
# * * * *

n = int(input("enter a number: "))
for i in range(n+1):
    for j in range(n):
        print("*", end=" ")
    print()
    

# TASK 6: Inverted Triangle
# User se rows 'n' input lo aur ye pattern print karo:
# * * * *
# * * *
# * *
# *
y = int(input("enter a number: "))
for j in range(y+1,0,-1):
    pattern =( "*" * j)
    print(pattern)
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
