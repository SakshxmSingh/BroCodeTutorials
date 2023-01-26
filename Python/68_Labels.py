import tkinter

# label = an area widget that holds text and/or an image within a window

window = tkinter.Tk()

photo = tkinter.PhotoImage(file='Screenshot 2022-10-12 120239.png')


label = tkinter.Label(window,                                       # window in which the label would go
                      text="Hello world",
                      font=('Arial', 32, 'bold'),
                      fg='#00FF00',                                 # label foreground color, accepts color name and hex codes
                      bg='black',                                   # label background color
                      relief='raised',                              # border relief
                      bd=10,                                        # border thickness
                      padx=20,                                      # padding around the text in label in x axis
                      pady=20,                                      # padding around the text in label in y axis
                      image=photo,                                  # adds image to label
                      compound='bottom')                            # compounds text and image


label.pack()                                                        # places the label in centre top by default
# label.place(x=100, y=100)                                         # places the label at a particular coordinates


window.mainloop()
