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

# Lists in Python
# A built-in data type that stores set of values
# It can store elements of different types (integer, float, string, etc.)
marks = [94.3, 92.6, 88.8, 78.9]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])

# Lists are mutable
student = ["Karan", 98.5, 17, "Delhi"]
print(student[0])
student[0] = "Jeax"
print(student)

# List Slicing (Similar to string slicing)
marks = [88, 78, 90, 79, 97, 95]
marks = marks[0:5]
print(marks)

# List Methods
list = [2, 1, 3]
print(list.append(4))
print(list.sort())
print(list.sort(reverse=True))
print(list)

list = [2, 1, 3]
list.insert(1,5)
list.reverse()
print(list)

list = [2, 1, 3, 4]
list.pop(2)
print(list)