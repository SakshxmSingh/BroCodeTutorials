import tkinter

# button = you click it, it does stuff

count = 0

def click():
    global count
    count += 1
    print("You clicked the button",count,"times")


window = tkinter.Tk()
photo = tkinter.PhotoImage(file='Screenshot 2022-10-12 120239.png')


button = tkinter.Button(window,
                        text="Click me!",
                        command=click,                                  # function to run when button is clicked
                        font=('Comic Sans', 15),
                        fg='#00FF00',
                        bg='black',
                        activeforeground='#00FF00',
                        activebackground='black',
                        state='active',
                        # image=photo,
                        # compound='top',

                        )

button.pack()

window.mainloop()
