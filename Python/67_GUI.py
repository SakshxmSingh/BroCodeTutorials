import tkinter

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = tkinter.Tk()                        # instantiate an instance of a window
window.geometry("420x420")                   # to give dimensions to the window
window.title("Saksham First GUI program")    # to change the title of the gui window

icon = tkinter.PhotoImage(file='Screenshot 2022-10-12 120239.png')      # turns the image into photoimage, only compatible format
window.iconphoto(True, icon)                 # to apply the photoimage as the icon
window.config(background="black")            # change background color of window, also accepts hex values

window.mainloop()                            # places window on the computer screen, listen for events
