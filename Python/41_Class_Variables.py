from cars import Car                    # cars.py also used

car1 = Car("Chevy", "Corvette", 2022, "Black")
car2 = Car("Lamborghini", "Gallardo", 2016, "Green")

print(Car.wheels)                       # returns the default value of class variable
print(car1.wheels)
print(car2.wheels)

car1.wheels = 2                         # class variables can be individually modified per object
print(car1.wheels)
print(car2.wheels)

Car.wheels = 2                          # changing the default will change it for every object
print(Car.wheels)                        
print(car1.wheels)
print(car2.wheels)
