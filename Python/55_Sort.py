# sort() method       = used with lists
# sorted() function   = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

students.sort()                                                    # sort() method, sorts in alphabetical order
for i in students:
    print(i)
print("----------------------------------------------")

students.sort(reverse=True)                                        # sorts in reverse alphabetical order
for i in students:
    print(i)
print("----------------------------------------------")


# for tuples

teachers = ("Heisenberg", "Doofenshmritz", "Joker", "Homelander", "Harlynn Quinzel")

sorted_teachers = sorted(teachers)                                 # sorted() function
for i in sorted_teachers:
    print(i)
print("----------------------------------------------")

sorted_teachers = sorted(teachers, reverse=True)
for i in sorted_teachers:
    print(i)
print("----------------------------------------------")


# for 2d list of tuples

students = [
            ("Squidward", "F", 60),                                # format of name, grade, age
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)
            ]

students.sort()                                                    # will sort on the basis of the first column only
for i in students:
    print(i)
print("----------------------------------------------")

grade = lambda grades: grades[1]                                   # where grade is a function object returning index[1]
students.sort(key=grade)                                           # will sort on the basis of index[1] of each tuple
for i in students:
    print(i)
print("----------------------------------------------")

age = lambda ages: ages[2]                                         # where grade is a function object returning index[2]
students.sort(key=age)                                             # will sort on the basis of index[2] of each tuple
for i in students:
    print(i)
print("----------------------------------------------")


# for 2d tuple of tuple

sorted_students = sorted(students)                                  # first column
for i in sorted_students:
    print(i)
print("----------------------------------------------")

sorted_students = sorted(students, key=grade)                       # second column
for i in sorted_students:
    print(i)
print("----------------------------------------------")

sorted_students = sorted(students, key=age)                         # third column
for i in sorted_students:
    print(i)
print("----------------------------------------------")