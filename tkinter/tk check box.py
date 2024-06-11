from tkinter import *

root = Tk()
root.geometry("400x400")

var = IntVar()
var.set(1) # 🐾toggle between 0 or 1

c = Checkbutton(root, text= "Check this box", variable= var)
# var indicate 复选框当前的状态值（0 或 1）
c.pack()

def show_option():
    label.config(text=f"Option is: {var.get()}")

# Create a label once
label = Label(root, text=f"Option is: {var.get()}")
label.pack()

button = Button(root, text= "show option", command= show_option)
button.pack()

root.mainloop()