# Nested loop = a loop within a loop
#               all iterations of inner loop will execute first before executing one of the outer loop, and repeat

rows, columns, symbol = "", "", ""

while rows == "":
    rows = input("Enter no of rows: ")
rows = int(rows)
while columns == "":
    columns = (input("Enter no of columns: "))
columns = int(columns)
while len(symbol) == 0:
    symbol = input("Enter symbol to make rectangle of: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()
