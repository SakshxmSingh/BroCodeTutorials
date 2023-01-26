# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression (if/else) for item in iterable]


# -----------creating new list--------------------#

# classic method
squares = []                    # create an empty list
for i in range(1, 11):          # create a for loop
    squares.append(i*i)         # define what each loop iteration should do
print(squares)


# list comprehension method
squares = [i*i for i in range(1, 21)]                               # same as above
print(squares)


# --------------mimic lambda fnc-----------------#

# classic method
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# list comprehension method
passed_students = [i for i in students if i >= 70]                            # conditional
print(passed_students)

passed_students = [(i if i >= 70 else "FAILED") for i in students]              # if-else
print(passed_students)
