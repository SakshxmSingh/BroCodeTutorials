# exception = events detected during execution that interrupt the flow of a program

try:                                                                # to try a block of code
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:                                      # to execute block of code when running in an error
    print(e)
    print("you cant divide by zero idiot")
except ValueError as e:                                             # '...as e' allows to return the error statement to a str variable
    print(e)
    print("enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:                                                            # always execute whether run into an error or not
    print("This will always execute")
