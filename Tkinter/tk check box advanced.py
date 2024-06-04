from tkinter import *

root = Tk()
root.geometry("400x400")

var = StringVar()
var.set("start") # 🐾toggle between 0 or 1

c = Checkbutton(root, text= "Check this box", variable= var, onvalue="On", offvalue="Off")
# var = IntVar()中的 var indicate 复选框当前的状态值（0 或 1）
# var = StringVar()中的 var indicate onvalue or offvalue, 🧪未指定onvalue or offvalue時 var indicate check status(0 or 1)
c.deselect()
c.pack()

def show_option():
    label.config(text=f"Option is: {var.get()}")

# Create a label once
label = Label(root, text=f"Option is: {var.get()}")
label.pack()

button = Button(root, text= "show option", command= show_option)
button.pack()

root.mainloop()