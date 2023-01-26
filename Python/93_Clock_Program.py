from tkinter import *
import time

def update():
    time_string = time.strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    day_string = time.strftime('%A')
    day_label.config(text=day_string)

    date_string = time.strftime('%B %d, %Y')
    date_label.config(text=date_string)

    window.after(100, update)                               # a function to call another function after certain time(ms)

window = Tk()

window.config(bg='black')

time_label = Label(window, font=("Times New Roman", 40), fg='#00FF00', bg='black')
time_label.pack()

day_label = Label(window, font=("Times New Roman", 20), fg='#00FF00', bg='black')
day_label.pack()

date_label = Label(window, font=("Times New Roman", 22), fg='#00FF00', bg='black')
date_label.pack()

update()

window.mainloop()
