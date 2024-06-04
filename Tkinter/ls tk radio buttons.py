from tkinter import *

root = Tk()

var = IntVar()
# var.set() # 初始選擇. r.set(value) 设置 IntVar 的值, 這裏指value

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

Radiobutton(root, text= "Option1", variable=var, command=lambda: clicked(var.get())).pack() # ❓這裏的r.get()不就是1嗎
Radiobutton(root, text= "Option2", variable=var, command=lambda: clicked(var.get())).pack()
Radiobutton(root, text= "Option3", variable=var, command=lambda: clicked(var.get())).pack()
# var indicate the value of radio button
# 每个 Radiobutton 都与 IntVar 变量 var 绑定，并且有各自的值。当选择某个单选按钮时，r 的值会更新为相应的值，并触发 clicked 函数更新标签。

my_label = Label(root, text=var.get()) # var.get() 获取 IntVar 当前的值
my_label.pack()

my_button = Button(root, text="Click me!", command= lambda: clicked(var.get()))
my_button.pack()

root.mainloop()