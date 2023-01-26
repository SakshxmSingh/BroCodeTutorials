# super() = Function used to give access to the methods of parent class
#           Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class Square(Rectangle):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        return self.length*self.breadth

class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return self.length*self.breadth*self.height

square = Square(3, 3)
cube = Cuboid(3, 3, 3)

Square.area(square)
Cuboid.volume(cube)

print(square.area())
print(cube.volume())


