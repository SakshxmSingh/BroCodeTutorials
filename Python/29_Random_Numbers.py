import random

x = random.randint(1, 6)                    # random integer between the given argument
y = random.random()                         # random floating value between 0-1

mylist = ['rock', 'paper', 'scissors']
z = random.choice(mylist)                   # returns random argument from a list/set/tuple

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)                       # shuffles the contents of a list/tuple

print(x, y, z,cards)
