from tkinter import *
import time


WIDTH = 500                                                                     # making a constant which cant be changed later
HEIGHT = 500
xVelocity = 2
yVelocity = 1

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_image_space = PhotoImage(file='space.png')
my_image_space = canvas.create_image(0, 0, image=photo_image_space, anchor='nw')

photo_image = PhotoImage(file='ufo.png')
my_image = canvas.create_image(0, 0, image=photo_image, anchor='nw')

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()                                                             # to update the window after every while cycle
    time.sleep(0.01)

