# Expression Execution
# Numeric values can operate wuth all arithmetic operators
A,B = 2,3
C = 4
print(A+B*C) # B*C = 12 + A | Logic: Multiplication (*) takes priority over Addition (+)
# Arithmetic expression with Integer and float will result in float
A,B = 10,5.0
C = A*B
print(C)
# Result of division operator with two integers will be float
A,B = 1,2
C = A/B
print(C)
# Integer Division with float and int will give int displayed as float
A,B = 1.5,3
C = A//B
print(C,A/B)
# floor gives closest integer, which is lesser than or equal to the float value
# Result of (A//B) is same as floor (A/B)
A,B = 12,5
C = A//B
print(C)
A,B = -12,5
C = A//B
print(C)
A,B = 12,-5
C = A//B
print(C)
# Remainder is negative when denominator is negative
A,B = -5,2
C = A%B
print(C)
A,B = 5,2
C = A%B
print(C)
A,B = 5,-2
C = A%B
print(C)
# Comments in Python 
#single line comment
"""This is
a multi-line
comment"""
# Input in Python 
# input()statement is used to accept values (using keyboard) from user 
# string input
name = input("Name : ")
# int input
age = int(input("Age : "))
# float input
price = float(input("Price : "))
print(f"My Name is {name}, i am {age} years old and i buy a things of amount of {price} Rs.")
