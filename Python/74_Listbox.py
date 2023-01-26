# listbox = A listing of selectable text items within its own container

import tkinter

def submit():
    # print("You ordered", listbox.get(listbox.curselection()))                   # listbox.curselection() ---> returns the current selection, for single selection

    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You ordered ", end="")
    for i in food:
        print(i, end=" ")

def add():
    listbox.insert(listbox.size()+1, entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())                                      # to delete, for single selection

    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = tkinter.Tk()

listbox = tkinter.Listbox(window,
                          bg='#F7FFDE',
                          font=('Constantia', 18),
                          width=12,
                          selectmode='multiple'

                          )
listbox.pack()

listbox.insert(1, "pizza")                                                      # insert an element in the list a particular index
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())                                           # listbox.size() returns the height of listbox according to the elements in the list

entrybox = tkinter.Entry(window)
entrybox.pack()

add = tkinter.Button(window, text="Add", command=add)
add.pack()

delete = tkinter.Button(window, text="Delete", command=delete)
delete.pack()

submit = tkinter.Button(window, text="Submit", command=submit)
submit.pack()


window.mainloop()
