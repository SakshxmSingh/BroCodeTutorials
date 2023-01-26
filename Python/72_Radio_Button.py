# radio button = similar to checkbox, but you can only select one from a group

import tkinter

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == "pizza":
        print("You ordered pizza")
    elif x.get() == "hamburger":
        print("You ordered hamburger")
    elif x.get() == "hotdog":
        print("You ordered hotdog")

window = tkinter.Tk()

x = tkinter.StringVar()

for i in food:
    radiobutton = tkinter.Radiobutton(window,
                                      text=i,                   # adds text to radio buttons
                                      variable=x,               # groups radiobuttons together if they share the same variable
                                      value=i,                  # assigns each radibutton a different value
                                      padx=25,
                                      font=('Impact', 50),
                                      indicatoron=False,        # eliminate circle indicators
                                      width=12,                 # sets width of radio buttons
                                      command=order

                                      )
    radiobutton.pack(anchor='w')

window.mainloop()
