from tkinter import *
from tkinter import filedialog

window = Tk()

def openfile():
    filepath = filedialog.askopenfilename(title='Open file',            # filedialog.askopenfilename() returns a string with file path selected
                                          initialdir="C:\\Users\\saksh\\PycharmProjects\\BroCodeTutorials",  # initial default open folder
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*"))          # file formats requested
                                          )
    file = open(filepath, 'r')
    print(file.read())
    file.close()


button = Button(window, text='Open', command=openfile)
button.pack()

window.mainloop()
