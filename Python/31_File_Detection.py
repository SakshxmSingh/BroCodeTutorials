import os

path = "C:\\Users\\saksh\\Downloads\\WhatsApp Image 2022-07-17 at 2.31.07 PM.jpeg"
#                                                   # double back-slashes for python to read

if os.path.exists(path):                            # checks if location exists locally
    print("That location exists")
    if os.path.isfile(path):                        # checks if the location is a file
        print("That is a file")
    elif os.path.isdir(path):                       # checks if the location is folder/directory
        print("That is a directory")
else:
    print("That location doesnt exist")
