# entry widget = textbox that accepts a single line of user input

import tkinter

window = tkinter.Tk()

entry = tkinter.Entry(window,                               # entry x
                      font=('Arial', 30),
                      fg='#00FF00',
                      bg='black',
                      # show="*"                            # to show a particular character over every character
                      )

# entry.insert(0,'Spongebob')                               # enter a default text
entry.pack(side='left')

def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state='disabled')                          # to disable the entry box after typing the input once

def delete():
    entry.delete(0, 'end')

def backspace():
    entry.delete(len(entry.get())-1, 'end')


submit_button = tkinter.Button(window, text="submit", command=submit)
submit_button.pack(side='right')


delete_button = tkinter.Button(window, text="delete", command=delete)
delete_button.pack(side='right')

backspace_button = tkinter.Button(window, text="backspace", command=backspace)
backspace_button.pack(side='right')

window.mainloop()
