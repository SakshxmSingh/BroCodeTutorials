from tkinter import *
from tkinter import messagebox                 # sub module

window = Tk()

def click():
    # messagebox.showinfo(title='Message', message='Fuck you')                              # displays info icon
    # messagebox.showerror(title='Error', message='Something went wrong.')                  # displays error icon
    # while(True):
    #     messagebox.showwarning(title='WARNING!!!', message='You have a VIRUS!!!')         # displays warning icon

    # if messagebox.askokcancel(title='ask ok cancel', message='do you want to do the thing?') is True:
    #    print('You did the thing')
    # else:
    #    print('You canceled the thing')

    if messagebox.askretrycancel(title='ask retry cancel', message='do you want to retry the thing?') is True:
        print('You retried the thing')
    else:
        print('You canceled the thing')


button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
