# scope = The region in which a variable is recognized
#         A variable is only variable from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = "Saksham"                    # global scope (available both inside & outside functions)


def display_name():
    name = "Code"                   # local scope (available only inside the function)
    print(name)


print(name)
display_name()
