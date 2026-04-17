# Super method
# super() method is used to access methods of the parent class.

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("Car stoped...")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.type = type
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("prius", "electric")
print(car1.type)

# class method
# A class method is bound to the class & receives  the class as an implicit first argument.
# Note static method can't access or modify class state & generally for utility.

class Person:
    name = "anonymos"
    # def changeName(self, name):
    #     self.__class__.name = "Rahul"
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)