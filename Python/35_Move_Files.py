import os

source = "C:\\Users\\saksh\\Desktop\\python test 1.txt"
destination = "C:\\Users\\saksh\\PycharmProjects\\BroCodeTutorials\\python test 1.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" not found")

# also works for a folder
