# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500,)

"""
canvas.create_line(0,0,500,500, fill='blue', width=5)                 # four nos = coordintates of two points from where tp where line is to be drawn
canvas.create_line(0,500,500,0, fill='red', width=5)

canvas.create_rectangle(100,150,400,350, width=5, outline='green')    # coordinates of top left and bottom right corner

points = [250,0,0,500,500,500]
canvas.create_polygon(points, fill='', outline='purple', width=5)     # a list can be used as coordinates too
canvas.create_arc(0,0,500,500, style='arc', extent=180, start=180, outline='yellow', width=5)

"""

canvas.create_arc(100,100,400,400, fill='red', extent=180, width=8)
canvas.create_arc(100,100,400,400, fill='white', extent=180, start=180, width=8)
canvas.create_oval(210,210,290,290, fill='white', width=8)


canvas.pack()

window.mainloop()
