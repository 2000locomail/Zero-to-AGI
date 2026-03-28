# Recursion
# When a Function calls itself repetedly.

def show(n):
    if (n == 6):
        return
    print(n)
    show(n+1)
    print("END")
show(1)

def fact(n):
    if (n == 0 or n== 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

# Let's Practice
# Write a recursive function to calculate the sum of first n natural numbers.
def sum_f_n(n):
    if (n == 0):
        return 0
    return n + sum_f_n(n-1)

print(sum_f_n(3))

# Write a recursive function to print all elements in a list

def print_list(list,idx = 0):
    if (idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banana"]
print_list(fruits)