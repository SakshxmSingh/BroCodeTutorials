"""
>> Python Calculator
"""

from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))                            # eval() evaluates

        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_text = "Can't divide by zero"
        equation_label.set(equation_text)

    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator Program")
window.geometry("500x500")
window.config(bg='#dedede')

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('bahnschrift', 20), bg='white', width=24, height=2, relief='ridge', bd=4)
label.pack()

frame = Frame(window)
frame.pack()

#--------------------------------------------------num-pad buttons----------------------------------------------------#

Button(frame, text=7, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(7)).grid(row=0, column=0)
Button(frame, text=8, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(8)).grid(row=0, column=1)
Button(frame, text=9, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(9)).grid(row=0, column=2)
Button(frame, text='/', width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press('/')).grid(row=0, column=3)
Button(frame, text=4, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(4)).grid(row=1, column=0)
Button(frame, text=5, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(5)).grid(row=1, column=1)
Button(frame, text=6, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(6)).grid(row=1, column=2)
Button(frame, text='*', width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press('*')).grid(row=1, column=3)
Button(frame, text=1, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(1)).grid(row=2, column=0)
Button(frame, text=2, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(2)).grid(row=2, column=1)
Button(frame, text=3, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(3)).grid(row=2, column=2)
Button(frame, text='-', width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press('-')).grid(row=2, column=3)
Button(frame, text='.', width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press('.')).grid(row=3, column=0)
Button(frame, text=0, width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press(0)).grid(row=3, column=1)
Button(frame, text='=', width=9, height=4, font=('bahnschrift', 12), command=equals).grid(row=3, column=2)
Button(frame, text='+', width=9, height=4, font=('bahnschrift', 12), command=lambda: button_press('+')).grid(row=3, column=3)

#------------------------------------------------------------------------------------------------------------------------#

Button(window, text='Clear', width=10, height=3, font=('bahnschrift', 11), command=clear).pack()


window.mainloop()
