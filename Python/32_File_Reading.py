# ---------------correct with no exception handling------------------------------- #
# with open("C:\\Users\\saksh\\Desktop\\python test 1.txt") as file:
#    print(file.read())

try:
    with open("C:\\Users\\saksh\\Desktop\\python test 1.txt") as file:      # assigns the content of file to a variable
        print(file.read())
except FileNotFoundError:
    print("That file was not found")