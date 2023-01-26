
text = "Lessss gooooooooooooo \nI pull upp\n"

with open('python test 2.txt', 'w') as file:            # 'w' to write
    file.write(text)

text = "Have a nice day"
with open('python test 2.txt', 'a') as file:            # 'a' to append, cant use 'w' as it would overwrite the previous
    file.write(text)
