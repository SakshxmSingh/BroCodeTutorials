
fs = [0, 1]

while len(fs) <= 19:
    fs.append(fs[len(fs) - 2] + fs[len(fs) - 1])

for i in fs:
    print(i)
