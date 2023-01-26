# OOP = Object-Oriented Programming, a computer programming model that organizes software design
#       around data, or objects, rather than functions and logic

# from cars import Car                                  # imported a class from another module, used cars.py

class Car:
    wheels = 4                                                     # class variable (common with all objects of class)

    def __init__(self, make, model, year, color):                  # makes the objects with the given arguments
        #                                                          # the 'constructor'
        #                                                          # self.'' refers to the traits of the object
        self.make = make
        self.model = model                                         # instance variables
        self.year = year
        self.color = color

    def drive(self):                                               # the methods/actions for our object
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

car1 = Car("Chevy", "Corvette", 2022, "Black")        # arguments to create the object, as in the def __init__() method
car2 = Car("Lamborghini", "Gallardo", 2016, "Green")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()                                          # methods for the assigned class Car
car1.stop()

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color)

car2.drive()
car2.stop()

print(car2.wheels)