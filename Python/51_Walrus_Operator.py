# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# --------------------example 1----------------------- #

# happy = True
# print(happy)

print(happy := True)                                                # same as above
print("---------------------------------------")

# --------------------example 2----------------------- #

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food.lower() == "quit":
#         break
#     foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":          # same as above
    foods.append(food)
