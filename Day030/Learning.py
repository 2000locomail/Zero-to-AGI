# del Keyword
# Used to delete object properties or object itself.
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Jeax")
print(s1.name)
del s1.name
print(s1.name)

# Private(like) attributs & methods
# Conceptual lmplementation in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcd")
print(acc1.reset_pass)
print(acc1.acc_no)
print(acc1.__acc_pass)

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())

# Inheritance
# When one class (child/derived) derives the properties & methods of another class (Parent/base).
# Types, 1. Single inheritance 
class Car:
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("Car stoped...")

class ToyataCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyataCar("fortuner")        
car2 = ToyataCar("prius")

print(car1.start())

# 2. Multi-level Inheritance 

class Car:
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("Car stoped...")

class ToyataCar(Car):
    def __init__(self, brand):
        self.name = brand

class Fortuner(ToyataCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

# 3. Multiple Inheritance

class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
