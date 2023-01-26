# index operator [] = gives access to a sequence’s element (str,list,tuples)

name = "Saksham Singh!"

if name[0].islower():
    name = name.capitalize()

first_name = name[0:7].upper()
last_name = name[8:].lower()
last_char = name[-1]

print(name)
print(first_name)
print(last_name)
print(last_char)
