# Function in Python

# function definition
def calc_sum(a, b): # parameters
    sum = a + b
    print(sum)
    return sum
calc_sum(2,4) # function call; arguments
#
def calculate_sum (a, b):
    return a + b

sum = calculate_sum(1,3)
print(sum)
#
def print_hello():
    print("hello")

print_hello()

output = print_hello()
print(output)

# averade of 3 numbers
def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return(avg)
calc_avg(76,82,79)

# Bilt-in function
print ("apna","college") # Sep = " "
print ("Satyam") # end = "\n"
print ("apnacollege", end = "$")
print ("Satyam")\

# User defined Function
# (By programer)

# Default Parameters
# Assibning a default value to parameter, which is used when no argument is passed 
def cal_prod(a=1, b=1):
    print(a * b)
    return a*b
cal_prod()
#
def cal_prod(a, b=1):
    print(a * b)
    return a*b
cal_prod(8)
#
def cal_prod(a=1, b=1):
    print(a * b)
    return a*b
cal_prod(2,3)

# Let's Practice
cities = ["delhi", "gurgaon", "mumbai", "noida", "pune"]
def cities_len(list):
    print(len(list))
    
cities_len(cities)

cities = ["delhi", "gurgaon", "mumbai", "noida", "pune"]
def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)
print()

#
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(4)

#
def converter(usd_val):
    inr_val = usd_val*92
    print(usd_val, "USD =", inr_val, "INR")

converter(79)