import tkinter

def display():
    if x.get() == 1:
        print("You agree")
    else:
        print("You dont agree")

window = tkinter.Tk()

x = tkinter.IntVar()
# photo = tkinter.PhotoImage(file='Screenshot 2022-10-12 120239.png')
check_button = tkinter.Checkbutton(window,
                                   text="I agree to something",
                                   variable=x,                      # variable to assign the value of check or uncheck
                                   onvalue=1,                       # value returned to the integer if checked
                                   offvalue=0,                      # value returned to the integer if unchecked
                                   command=display,
                                   font=('Arial', 20),
                                   fg='#00FF00',
                                   bg='black',
                                   activebackground='black',
                                   activeforeground='#00FF00',
                                   padx=20,
                                   pady=20,
                                   # image=photo,
                                   # compound='left'
                                   )

check_button.pack()
window.mainloop()
