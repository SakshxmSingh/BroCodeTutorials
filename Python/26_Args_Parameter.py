# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# def add(num1, num2):
#     sum = num1 + num2
#     return sum
# print(add(1,2,3))                    #TypeError:add() takes 2 positional arguments but 3 were given, so it doesnt work


def add(*stuff):                       # args can be anything, * is important
    sum = 0
    # stuff[0] = 3                     # cant be assigned as TypeError: 'tuple' object does not support item assignment
    stuff = list(stuff)                # typecasting stuff to list, now it can be edited
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(add(2, 4, 5, 6, 8))              # the arguments here make up the arguments in *stuff
#                                        value of 2 is not considered as 0 is already assigned in the list above at [0]
