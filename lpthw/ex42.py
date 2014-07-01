#!/usr/bin/env python3

class Animal(object):
    
    def __init__(self,noise):
        self.noise = noise

    def sound(self):
        print(self.noise)


class Dog(Animal):
    
    def __init__(self, name, noise):
        self.name = name
        super(Dog, self).__init__(noise)

    def woof(self):
        print("woof")


class Cat(Animal):

    def __init__(self, name, noise):
        self.name = name
        super(Cat, self).__init__(noise)

    def meow(self):
        print("meow")


class Person(object):
    
    def __init__(self, name):
        self.name = name;
        self.pet = None


class Employee(Person):
    
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):

    pass


class Salmon(Fish):

    pass


class Halibut(Fish):

    pass


rover = Dog("Rover","bark")
satan = Cat("Satan","grrr")

mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank",120000)
frank.pet = rover

flipper = Fish()
crouse = Salmon()
harry = Halibut()

rover.woof()
rover.sound()
satan.meow()
satan.sound()
