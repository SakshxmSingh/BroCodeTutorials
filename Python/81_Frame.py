# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg='pink', bd=5, relief='sunken')                           # to make a frame
frame.place(x=0, y=0)                                                             # to place the coordinates

Button(frame, text="W", font=("Consolas", 25), width=3).pack(side='top')
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side='left')
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side='left')
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side='left')

window.mainloop()
