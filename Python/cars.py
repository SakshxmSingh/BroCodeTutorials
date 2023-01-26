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

def drive():
    pass
