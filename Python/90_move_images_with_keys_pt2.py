# to move images on a canvas
from tkinter import *

def up(event):
    canvas.move(myimage, 0, -5)                # .move() takes 3 args--> the widget, and the coordinates to move by

def left(event):
    canvas.move(myimage, -5, 0)

def down(event):
    canvas.move(myimage, 0, 5)

def right(event):
    canvas.move(myimage, 5, 0)

window = Tk()

window.bind("<w>", up)
window.bind("<a>", left)
window.bind("<s>", down)
window.bind("<d>", right)
window.bind("<Up>", up)
window.bind("<Left>", left)
window.bind("<Down>", down)
window.bind("<Right>", right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file='racecar.png')
myimage = canvas.create_image(0,0,image=photoimage, anchor='nw')

window.mainloop()
