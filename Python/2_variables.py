# variable = a container for a value. and it behaves like the value it contains

first_name = "Saksham"                                  # string
last_name = "Singh"
full_name = first_name + " " + last_name
print(type(full_name))                                  # type() function ----> prints type of variable


age = 18                                                # integer
age += 1                                                # same as "age = age + 1"
print(age)
print(type(age))


height = 174.5                                          # float
print(height)
print(type(height))

human = False                                           # boolean
print(human)
print(type(human))


print("Hello " + full_name)
print("Your age is " + str(age))
#                                                # a str and int cannot be printed together, so "str()" is used to change type to str from int
print("Your height is " + str(height) + " cms")         # same as above
print("Are you an alien: " + str(human))
