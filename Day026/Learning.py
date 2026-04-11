# __init__ Function
# Constructor
# All classes have a function called __init_(),which is always executed when the object is being initiated.
class Student:
    def __init__(self, fullname):
        self.name = fullname
        print(self)
        print("adding new student in database...")


# creating objects (instance)
s1 = Student("Karan")
print(s1.name)