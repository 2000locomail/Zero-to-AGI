# ---------------------------------------------------------
# LEVEL 3: NESTED LOOPS (Patterns & Grids)
# ---------------------------------------------------------

# TASK 5: Square Star Pattern
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
# * * * *
# * * *
# * *
# *
y = int(input("enter a number: "))
for j in range(y+1,0,-1):
    pattern =( "*" * j)
    print(pattern)
