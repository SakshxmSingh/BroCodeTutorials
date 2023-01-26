# grid() = geometry manager that organises widgets in a table-like structure in a parent window

from tkinter import *

window = Tk()

Label(window, text="Enter your info").grid(row=0, columnspan=2)

Label(window, text="First name: ").grid(row=1, column=0)                # grid() used instead of pack()
Entry(window).grid(row=1, column=1)

Label(window, text="Last name: ").grid(row=2, column=0)
Entry(window).grid(row=2, column=1)

Label(window, text="Email ").grid(row=3, column=0)
Entry(window).grid(row=3, column=1)

Button(window, text="Submit").grid(row=4, column=0, columnspan=2)       # columnspan= specifies how many columns a widget occupies in case of merging

window.mainloop()
