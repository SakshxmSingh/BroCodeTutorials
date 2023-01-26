from tkinter import *

def doSomething(event):
    print("You pressed: "+event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", doSomething)                   # bind() binds an event to a function for the window/file. format --> ("<keyboard event>", function). Key for all keys

label = Label(window, font=("Helvetica",50))
label.pack()

window.mainloop()
