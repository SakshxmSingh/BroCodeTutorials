import tkinter

def submit():
    print("The temperature is", scale.get(), "degrees C")

window = tkinter.Tk()

scale = tkinter.Scale(window,
                      from_=100,                          # starting point of scale
                      to=0,                               # max point of scale
                      length=500,                         # length of scale
                      orient='vertical',                  # orientation of scale
                      font=('Consolas', 14),
                      tickinterval=10,                    # to display text at every interval of __, adds numerical indicators
                      showvalue=True,                     # show/hide current value
                      resolution=5,                       # increment of slider
                      troughcolor="#69EAFF",              # color of scale bar
                      fg='#FF1C00',
                      bg='black'

                      )
scale.set((scale['from']-scale['to'])/2 + scale['to'])    # set default value of slider
scale.pack()

button = tkinter.Button(window,
                        text='submit',
                        command=submit
                        )
button.pack()


window.mainloop()
