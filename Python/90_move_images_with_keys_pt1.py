# to move images in a window

from tkinter import *

def up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-5)                         # placing the widget to the given coordinates

def left(event):
    label.place(x=label.winfo_x()-5, y=label.winfo_y())

def down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+5)

def right(event):
    label.place(x=label.winfo_x()+5, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>", up)
window.bind("<a>", left)
window.bind("<s>", down)
window.bind("<d>", right)
window.bind("<Up>", up)
window.bind("<Left>", left)
window.bind("<Down>", down)
window.bind("<Right>", right)

myimage = PhotoImage(file='racecar.png')

label = Label(window, image=myimage)
label.place(x=0, y=0)

window.mainloop()
