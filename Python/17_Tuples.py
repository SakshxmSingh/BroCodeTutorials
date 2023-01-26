# tuple = collection that is ordered and unchangeable
#         used to group together related data

student = ("Saksham", 18, "Male")

print(student.count("Saksham"))                      # prints count of particular element
print(student.index(18))                             # prints index of given element

for x in student:
    print(x, end=", ")
