# Lists = used to store multiple values in one variable, same as arrays

cars = ["Tesla", "Lambo", "Camaro", "Ferrari"]
print(cars[1])
cars[1] = "McLaren"
print(cars[1])

cars.append("RolceRoyce")                   # adds an element
cars.remove("Tesla")                        # removes an element
cars.pop()                                  # removes last element
cars.insert(1, "Ford")                      # insert element at given index
cars.sort()                                 # sort in alphabetical order
cars.clear()                                # clears the list

for x in cars:
    print(x)
