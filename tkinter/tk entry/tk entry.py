# 🔢get(): 获取Entry字段当前的内容。
    # 此方法不接受任何参数，返回字符串类型，表示当前输入框中的文本。
# 🔢insert(index, string):
    # 在指定的index位置插入string。如果index等于END或tkinter.END，则文本被追加到输入框的末尾
# 🔢delete(start_index, end_index=None):
    # 删除从start_index开始到end_index结束位置之间的文本。如果end_index未指定，则只删除start_index位置的字符。索引从0开始计数。
# 🔢config(options) 或 configure(options):
    # 用于更改Entry部件的配置选项，如颜色、字体等。options是一个字典，包含了要设置的属性及其值。
# 🔢focus_set():
    # 将输入焦点设置到该Entry部件上，使用户可以直接开始在其中输入。

import tkinter as tk

root = tk.Tk()

entry1 = tk.Entry(root, width= 50, bg="blue", fg="white", borderwidth=5)
# 預設文本
entry1.insert(0, "Enter your name:")
# e.insert(6, "abc") # 第一个参数是插入文本的位置
entry1.pack()

def myClick():
    entry1.delete(0, 1)
    myLabel = tk.Label(root, text = entry1.get())
    myLabel.pack()
myButton = tk.Button(root, text = "Click me!", fg = "blue", bg= "grey", command= myClick)
myButton.pack()

root.mainloop()