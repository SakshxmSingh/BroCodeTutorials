# multiple inheritance = when a child class is derived from more than one class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    def run(self):
        print("This rabbit is running")

class Fish(Prey, Predator):
    def swim(self):
        print("This fish is swimming")

class Hawk(Predator):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
