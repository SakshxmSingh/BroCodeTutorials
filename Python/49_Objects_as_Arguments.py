class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, paint):                               # accepts object as argument
    vehicle.color = paint                                       # to change an attribute of the object

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()
bike2 = Motorcycle()
bike3 = Motorcycle()

print(car1.color)
print(car2.color)
print(car3.color)

change_color(car1, "red")
change_color(car2, "blue")
change_color(car3, "yellow")

change_color(bike1, "green")
change_color(bike2, "black")
change_color(bike3, "white")

print(car1.color)
print(car2.color)
print(car3.color)

print(bike1.color)
print(bike2.color)
print(bike3.color)
