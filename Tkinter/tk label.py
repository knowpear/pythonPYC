from tkinter import *

root = Tk()

var = IntVar()
var.set(20)

def clicked(value):
    # my_label.config(text=r.get())
    my_label.config(text=f"your choice is: {var.get()}")

Radiobutton(root, text= "Option1", variable=var, value=10, command=lambda: clicked(var.get())).pack()
Radiobutton(root, text= "Option2", variable=var, value=20, command=lambda: clicked(var.get())).pack()
Radiobutton(root, text= "Option3", variable=var, value=30, command=lambda: clicked(var.get())).pack()


my_label = Label(root, text=f"your choice is: {var.get()}")
my_label.pack()

root.mainloop()