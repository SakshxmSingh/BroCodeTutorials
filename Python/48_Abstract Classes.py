# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has declaration but does not have an implementation

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

from abc import ABC, abstractmethod                     # abc ---> abstract based class

class Vehicle(ABC):                                     # Inheriting from ABC makes a class abstract

    @abstractmethod                                     # Declaring a method to be abstract
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):                                       # Abstract methods need to be overridden
        print("You drive the car")

    def stop(self):
        print("This car has stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle has stopped")

# vehicle = Vehicle()                      # TypeError: Can't instantiate abstract class Vehicle with abstract method go
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()

