# Set in Python
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

collection = {1,2,2,3,4, "Jeax", 5} # Duplicate values not allowed in set
print(type(collection))
print(len(collection))
print(collection) # Repeated elements stored only once, so it resolved to {1,2,3,4,5,etc}

empty_set = set() # empty set; syntax
print(type(empty_set))

# Set Methods

collections = set()

collections.add(1)
collections.add(2)
collections.add(3)
collections.remove(1)
collections.add("Jeax")
collections.add("India")
collections.add((1, 2, 3))
collections.pop()
print(collections)

collections.clear()


print(len(collections))

set1 = {1,2,3,4}
set2 = {3,4,5,6}
union = set1.union(set2)
intersection = set1.intersection(set2)
print(union)
print(intersection)

# Let's Practice

dictionary = {
    "table" :( "a piece of furniture", "list of facts & figures"),
    "cat" : "a small animal",
}
print(dictionary)

subject = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subject))

marks = {}
X = int(input("Enter Your phy marks: "))
marks.update({"phy" : X})

X = int(input("Enter Your math marks: "))
marks.update({"math" : X})

X = int(input("Enter Your chem marks: "))
marks.update({"chem" : X})

print(marks)
 
value = {9,"9.0"}
print(value)

value = {("float" , 9.0),
         ("int" , 9)}
print(value)