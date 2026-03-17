# Tuples in Python
# A built-in data type that lets us create immutable sequences of values
# A comma (,) is compulsory in tuple
tup = (2, 1, 3 ,1)
print(type(tup))
print(tup.index(1))
print(tup.count(1))
print(tup[0])
print(tup[1])

tup = ()
print(tup)

list = []
list.append(input("Enter Your 1 favorite movies name: "))
list.append(input("Enter Your 2 favorite movies name: "))
list.append(input("Enter Your 3 favorite movies name: "))
print(list)

list = [input("Enter Something: ")]
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")
else:
    print("NOT palindrome")

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)