# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)

print("The {} jumped over the {}".format(animal, item))       # same output as line above, {} acts as a placeholder
#                                                               called 'format-fields' for the object in format()
#                                                               these are positional arguments

print("The {1} jumped over the {0}".format(animal, item))     # positional argument, roles reversed with index reversing
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))
#                                                             # keyword argument

print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))  # same value can be usd more than once
print("The {1} jumped over the {1}".format(animal, item))       # same as above but positional arg.

# ---------------------------------------------- #

text = "The {} jumped over the {}"
print(text.format(animal, item))
# str variable can be formatted too

# ---------------------------------------------- #

name = "Saksham"
print("My name is {}".format(name))
print("My name is {:10}. Nice to meet you".format(name))        # add space to left or right by {:n} where n is space
print("My name is {:<10}. Nice to meet you".format(name))       # adds to right, left-aligned text
print("My name is {:>10}. Nice to meet you".format(name))       # adds to left, right-aligned text
print("My name is {:^10}. Nice to meet you".format(name))       # adds to both side, centre-aligned
print("My name is {name:^10}. Nice to meet you".format(name="Saksham"))     # for keyword/positional, precede the column

# ---------------------------------------------- #

number1, number2, number3 = 3.141589, 1000000000, 50

print("The number Pi is {}".format(number1))                     # no need to typecast to str
print("The number Pi is {:.2f}".format(number1))                 # {:.nf} formats the no of decimal places to return,
#                                                                 also rounds the decimal
print("The number is {:,}".format(number2))                      # {:,} adds comma to the number by international system
#
print("The number is {:b}".format(number3))                      # {:b} formats the number in binary
print("The number is {:o}".format(number3))                      # {:o} formats the number in octal
print("The number is {:X}".format(number3))                      # {:x/X} formats the number in hexadecimal
print("The number is {:E}".format(number3))                      # {:e/E} formats the number in scientific notation
