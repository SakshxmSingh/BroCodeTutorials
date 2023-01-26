import time

# for loop = a statement that executes its block of code a limited number of times
#                   while = unlimited
#                   for = limited

# for i in range(10):
#     print(i)                                # prints 0 to 9, the first 10 numbers

# for i in range(10):
#     print(i+1)                              # prints 1 to 10

# for i in range(50, 100):
#    print(i)                                  # prints 50 to 99

# for i in range(50, 100+1, 2):
#    print(i)                                  # prints 50 to 100 in steps of 2

# for i in "Saksham":
#    print(i)                                  # prints each letter individually

# -----------simple way with no time----------#
# for i in range(10, -1, -1):
#     print(i)
# print("Happy New Year!!")


for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("HAPPY NEW YEAR!!!")
