# Dictionary in Python
# Dictionary are used to store data values in key:value pairs
# They are unordered, mutable(Changeable) & don't allow duplicate keys
info = {
    "name" : "Jeax",
    "age"  : 18,
    "is_adult" : True,
    "marks": 94.4,
    "subjects" : ["python","C"],
    "topics" : ("dict", "set"),
}


info["age"] = 23
info["profile"] = "Developer"
print(info)

null_dict = {}
print(null_dict)

# Nested Dictionaries
student = {
    "name" : "shradha",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "math" : 99,
    }
}

print(student)
print(student["score"]["chem"])
print(student.keys())
print(list(student.keys()))
print(len(student))
print(list(student.values()))
print(list(student.items()))
print(list(student.get("score")))
student.update({"city" : "Tvarnip"})
print(student)