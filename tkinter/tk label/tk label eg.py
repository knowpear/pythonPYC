import tkinter as tk

root = tk.Tk()

var = tk.IntVar()
# 它是一个IntVar类型的对象。IntVar是Tkinter模块中的一个类，用于在图形用户界面中存储整数类型的变量。这个变量可以在界面的控件中显示和修改，通常与控件如Entry或Spinbox结合使用。
var.set(20)

def clicked(value):
    # my_label.config(text=r.get())
    my_label.config(text=f"your choice is: {var.get()}")

tk.Radiobutton(root, text= "Option1", variable=var, value=10, command=lambda: clicked(var.get())).pack()
tk.Radiobutton(root, text= "Option2", variable=var, value=20, command=lambda: clicked(var.get())).pack()
tk.Radiobutton(root, text= "Option3", variable=var, value=30, command=lambda: clicked(var.get())).pack()

my_label = tk.Label(root, text=f"your choice is: {var.get()}")
my_label.pack()

root.mainloop()