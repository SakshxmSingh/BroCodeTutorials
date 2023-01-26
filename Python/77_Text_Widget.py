"""
text widget = functions like a text area, you can enter multiple lines of text
"""

import tkinter

def submit():
    print(text.get('1.0', 'end'))

window = tkinter.Tk()

text = tkinter.Text(window,
                    bg='light yellow',
                    font=('Ink free', 20),
                    height=8,
                    width=20,
                    padx=20,
                    pady=20,
                    fg='red'
                    )
text.pack()

button = tkinter.Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()
