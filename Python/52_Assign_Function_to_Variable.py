def hello():
    print("Ello!!")

hello()
print(hello)                                                # displays the memory address
hi = hello                                                  # assigning function to a variable
print(hi)                                                   # displays the same memory address
hi()                                                        # now hi() works as hello()

# example 2
say = print                                                 # assigning the function to a variable
say("Whoa! I can't believe this works!!")                   # say() works as print()
