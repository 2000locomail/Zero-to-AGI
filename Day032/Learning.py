# Property
# We use @proper ty decorator on any method in the class to use the method as a property.
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.calcPercentage()

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)  
stu1.phy = 89
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)

# @property

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    #     self.calcPercentage()
        
    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(98, 97, 99)
print(stu1.percentage)  

stu1.phy = 89
print(stu1.percentage)

# Polymorphism : Operator Overloding
# When the same operator is allowed to have different meaning according to the context.

# Operators & Dunder functions

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex (newReal, newImg)   
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 2)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

