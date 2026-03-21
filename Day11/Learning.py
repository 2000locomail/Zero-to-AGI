# Loops in Python
# Loops are used to repeat instructions.
# while loops
count = 1
while count <= 5:
    print("Jeax")
    count += 1

i = 1
while i <= 100:
    print("hello", i)
    i += 1
# print numbers from 1 to 5
i = 5 
while i >= 1:
    print(i)
    i -= 1

print("Loop Ended") 

# Let's Practice

num = 1
while num <= 100:
    print(num)
    num += 1

num = 100
while num >= 1:
    print(num)
    num -= 1 

num = int(input("Enter the number you want the table of: "))
i = 1
while i <= 10:
    print(num*i)
    i += 1 

nums = int(input("Enter the number you want the square of: "))
i = 1
while i <= nums:
    print(nums**2)
    break

# traverse

square = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(square):
    print(square[idx])
    idx += 1 

# Break : uused to terminate the loop when encountered

square = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter number you want to found: "))

i = 0 # initialization
while i < len(square):
    if (square[i] == x ):
        print("Found at idx", i)
        break
    else:
        print("finding...")
    i += 1

# Continue: terminates execution in the current iteration & continues execution of the loop with thw next iteration.

i = 0 
while i <= 10:
    
    if(i%2 == 0):
        i += 1
        continue # skip
    print(i)
    i += 1

# Loops are used for sequetial traversal. for traversaing list, string, tuples etc.
# for loops
nums = [1,2,3,4,5]
for val in nums:
    print(val)

tup = (1,2,3,4,2,3,5,7,)
for num in  tup:
    print(num)

square = [1,4,9,16,25,36,49,64,81,100]
for el in square:
    print(el)


square = (1,4,9,16,25,36,49,64,81,100)
x = 49
idx = 0 # linear search
for el in square:
    if (el == x):
        print("number is found at idx: ",idx)
    idx += 1

# range()

for i in range(10): #range(stop)
    print(i)

for i in range(2, 10): #range(start, stop)
    print(i)

for i in range(2, 101, 2): #range(start, stop, step)
    print(i) # even

for i in range(1, 100, 2): #range(start, stop, step)
    print(i) # odd 

# Let's Practice
# using for & range()
# Print numbers from 1 to 100
for num in range(1,101):
    print(num)

# Print numbers from 100 to 1
for nums in range(100,0, -1):
    print(nums)

# Print the multiplication table of a number n.
n = int(input("Enter a Number: "))
for i in range(1,11):
    print(n*i)

# pass Statement
# pass is a null statement that does nothing. It is used as a placeholder for future code.
for el in range(10):
    pass

# Let's Practice
# find the sum of first n natural numbers. (Using while)
n = 5
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print("total sum = ",sum)

# find the factorial of first n natural numbers (using for)
n = int(input("Enter a number: "))

factorial = 1

for i in range(1,n+1):
    factorial *= i
print(f"factorial of {n} is = ",factorial)

