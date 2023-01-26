# Duck Typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck then it must be a duck"

class Duck:
    def walk(self):
        print("This duck is walking")
        return self

    def talk(self):
        print("This duck is quacking")
        return self

class Chicken:
    def walk(self):
        print("This chicken is walking")
        return self

    def talk(self):
        print("This chicken is clucking")
        return self

class Person:
    def catch(self, animal):
        animal.walk()\
            .talk()
        print("You caught the critter!")
        return self


duck = Duck()
chicken = Chicken()
sak = Person()

sak.catch(duck)
sak.catch(chicken)
