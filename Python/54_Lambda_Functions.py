# lamda function = function written in one line using lambda keyword
#                  accepts anny number of arguments, but only has one expression.
#                  (think of it as a shortcut)
#                  (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression


# ---------------------------------------------------------------
def double(x):
    return x*2
print(double(5))

double = lambda x: x*2                                  # same as above function
print(double(10))

multiply = lambda x, y: x*y                             # with two arguments
print(multiply(30, 40))

add = lambda x, y, z: x+y+z
print(add(23, 23, 23))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Saksham", "Singh"))

age_check = lambda age: True if age >= 18 else False
print(age_check(12))
