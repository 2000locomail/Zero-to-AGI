class Student:

    # defult constructors
    def __init__(self):
        pass

    # parameterize constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database...")

s1 = Student("Karan", 95)
print(s1.name, s1.marks)
s2 = Student("arjun",98)
print(s2.name, s2.marks)

# Class & Instance Attributes

class Student:
    college_name = "ABC College"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database...")

s1 = Student("Karan", 95)
print(s1.name, s1.marks, s1.college_name)

# Method
class Student:
    college_name = "ABC College"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student", self.name)
    def get_marks(self):
        return self.marks

s1 = Student("Karan", 95)
s1.welcome()
print(s1.get_marks)