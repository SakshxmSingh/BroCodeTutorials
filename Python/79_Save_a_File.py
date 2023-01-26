from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\saksh\\PycharmProjects\\BroCodeTutorials',       # opens window to save a file as
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("HTML File", ".html"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return
    file_text = str(text.get('1.0', 'end'))
    file.write(file_text)
    file.close()


window = Tk()

button = Button(window, text='save', command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
