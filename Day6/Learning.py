# Indexing
str = "Apna College"
ch = str[0]
print(ch)
print(str[5])

# Slicing
# Accessing parts of a string

str = "Apna College"
print(str[0:5])
print(str[0:len(str)])

# Negative Index

str = "Apple"
print(str[-5:])
print(str[-5:-2])

# String Functions 
str = "i am a coder."
print(str.endswith("er."))
print(str.capitalize())

str = "i am a coder."
str = str.capitalize()
print(str)

str = "i am a coder."
str = str.replace("o","a")
print(str)

str = "i am a coder."
str = str.find("o")
print(str)

str = "i am a coder."
str = str.count("a")
print(str)

str = "i am a coder."
str = str.count("a")
print(str)

name = input("Enter Your Name : ")
print(len(name))

str = "The Price of My Loptop is $ 623.3"
str = str.count("$")
print(str)
