import os

text = "Lessss gooooooooooooo \nI pull upp\n"

with open('text.txt', 'w') as file:            # 'w' to write
    file.write(text)

path = 'text.txt'

try:
    # os.remove(path)               delete a file
    # os.rmdir(path)                delete an empty directory
    # shutil.rmtree(path)           delete a directory containing files (need to import shutil module)
    if os.path.exists(path):
        os.remove(path)
        print(path+" was removed")
    else:
        print(path+" does not exist")

except FileNotFoundError:
    print(path+" does not exist")
