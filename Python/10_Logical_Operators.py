# logical operators (and,or,not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside today? "))

if 20 <= temp <= 30:
    print("It is pleasant today!")
elif temp >= 30:
    print("It is hot today")
elif temp <= 20:
    print("It is cold today")

if temp >= 30 or temp <= 20:
    print("Let's not go out")
else:
    print("let's go out!")
