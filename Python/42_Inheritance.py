class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):             # the class inside () is the parent, all methods of parent are passed down, code reuse
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)                         # inherited code
fish.eat()
hawk.sleep()

rabbit.run()                                # specific code
fish.swim()
hawk.fly()
