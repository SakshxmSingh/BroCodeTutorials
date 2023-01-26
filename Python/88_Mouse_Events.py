from tkinter import *

def doSomething(event):
    print("Mouse coordinates: "+str(event.x)+","+str(event.y))

window = Tk()

# window.bind("<Button-1>", doSomething)                    # Button-1 for left click
# window.bind("<Button-2>", doSomething)                    # scroll wheel button
# window.bind("<Button-3>", doSomething)                    # right click
# window.bind("<ButtonRelease>", doSomething)               # button release, whether right or left
# window.bind("<Enter>", doSomething)                       # coordinates of where the mouse enters the window
# window.bind("<Leave>", doSomething)                       # coordinates of where the mouse leaves the window
window.bind("<Motion>", doSomething)                        # where the mouse moves

window.mainloop()
