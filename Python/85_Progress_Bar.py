from tkinter import *
from tkinter.ttk import *                       # progress bar in ttk
import time

def start():
    GB = 200
    download = 0
    speed = 0.5
    while download < GB:
        time.sleep(0.1)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+"%")                                # .set =  set a VALUE to a variable
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()                                               # updates the window with every update of idle tasks

window = Tk()

percent = StringVar()                                                           # to construct a string variable
text = StringVar()

bar = Progressbar(window, orient='horizontal', length=400)                      # to make a progress bar
bar.pack(pady=10, padx=20)

Label(window, textvariable=percent).pack()                                      # label to display percentage
Label(window, textvariable=text).pack()

Button(window, text="Download", command=start).pack()

window.mainloop()
