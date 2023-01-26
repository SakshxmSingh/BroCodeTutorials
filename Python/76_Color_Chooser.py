from tkinter import *
from tkinter import colorchooser                      # submodule

def click():
    # color = colorchooser.askcolor()                 # asks the color, returns a tuple with RGB values and hex code
    # print(color)
    # colorHex = color[1]                             # to use the hex code
    # print(colorHex)
    window.config(bg=str(colorchooser.askcolor()[1])) # same as lines above but condensed

window = Tk()

window.geometry("420x420")

button = Button(text='click me', command=click)
button.pack()

window.mainloop()
