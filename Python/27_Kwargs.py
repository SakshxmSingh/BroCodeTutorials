# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept

def hello(**names):                                                 # kwargs can be anything, ** is important
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in names.items():
        print(value, end=" ")


hello(title="Mr.", first="Saksham", middle="Singh", last="Rana")
