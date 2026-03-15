# Type Conversion
a = int("2")
b = 4.25

sum = a + b # 2.0 + 4.25 => 6.25
print(sum)

# Input in Python
# input( statement is used to accept values (using keyboard) from user
name = input("Enter your Name : ")# result for input()is always a str
age = int(input("Enter your Age : ")) # int input
price = float(input("Enter your Product price : ")) # float
print(f"Welcome {name} , you are {age} years old nice and your porduct price is {price}.")

num1 = int(input(" Enter your Number : "))
num2 = int(input(" Enter your Number : "))

sum = num1+num2
print("sum = ",sum)

side = float(input("Enter Square side : "))
print("area = ", side**2)

a = float(input("Enter First : "))
b = float(input("Enter First : "))
print("Avg = ", (a+b)/2)

a = float(input("Enter First : "))
b = float(input("Enter First : "))
print(a >= b)

#Strings 
# String is data type that stores a sequence of characters
str1 = "This is a string.\nwe are creating it in python."
print(str1) # \n is for next line 
str2 = "This is a string.\twe are creating it in python."
print(str2) # \t is for tab space 
#Concatenation

str3 = "Hello"
str4 = "world"
final_str = str3+str4
print(final_str) #Helloworld

str23 = "Hello"
str24 = "world"
final_str = str23+" "+str24
print(final_str) #Hello World

# Length

str5 = "Hello"
len1 = len(str5)
print(len1)
str6 = "world"
len2 = len(str6)
print(len2)
