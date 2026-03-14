"""# Singal Line Conditional Statements
# Single Line if / Ternary Operator
food = input("food : ").lower()
eat = "Yes" if food == "cake" else "no"
print(eat)

food = input("food : ").lower()
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

# Clever if / Ternarry Operator
age = int(input("age : "))
vote = ("yes", "no") [age < 18]
print(vote)

sal = float(input("salary : "))
tax = sal*(0.1,0.2) [sal > 50000]
print(tax)

# Types of Operators
# An operator is a symbol that performs a certain aperation between operands.

# Arithmetic Operators (+,-,*,%,**,/)
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
sum = a + b
print(sum)
sum = a - b
print(sum)
sum = a / b
print(sum)
sum = a * b
print(sum)
sum = a % b # Remainder
print(sum)
sum = a ** b # a^b
print(sum)

# Relational | Comparison Operators (==,!=,>,<,>=,<=)

a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))
tf = a == b
print (tf)
tf = a != b
print (tf)
tf = a > b
print (tf)
tf = a < b
print (tf)
tf = a >= b
print (tf)
tf = a <= b
print (tf)

# Assingnment Operators (=,+=,-=,*=,/=,**=,%=)

num = 100
num += 10
print(num)
num = 100
num -= 10
print(num)
num = 100
num *= 10
print(num)
num = 100
num /= 10
print(num)
num = 100
num %= 10
print(num)
num = 100
num **= 10
print(num)

# LOgical Operators (not. and. or)
# not

a = 50
b = 30
print(not a > b)
print(not a < b)

# and

val1 = True
val2 = True
print("and operator : " ,val1 and val2)

# or

val1 = True
val2 = False
print("Or operator : " ,val1 or val2)
print("Or operator : " , (a==b) or (a>b))"""

# Type Conversion

