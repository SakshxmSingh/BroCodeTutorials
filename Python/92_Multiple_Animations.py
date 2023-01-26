from tkinter import *
import time

class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color, width=2)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)
        if coordinates[2] >= WIDTH or coordinates[0] < 0:
            self.xVelocity = -self.xVelocity
        if coordinates[3] >= HEIGHT or coordinates[1] < 0:
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)


WIDTH = 500
HEIGHT = 500

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='light blue')
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 3, 2, 'white')
tennis_ball = Ball(canvas, 0, 0, 30, 6, -2, 'light green')
basket_ball = Ball(canvas, 0, 0, 120, 3, 3, 'orange')
cricket_ball = Ball(canvas, 0, 0, 50, -4, 5, 'red')

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    cricket_ball.move()
    window.update()
    time.sleep(0.01)

