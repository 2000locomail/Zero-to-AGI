# Static Methods
# Methods that don't use the self parameter (work at class leve)
class Student:
    @staticmethod
    def college():
        print("ABC College")
s1 = Student()
s1.college()