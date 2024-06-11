# 📚[Tkinter Label](https://www.tutorialspoint.com/python/tk_label.htm)
# Syntax: w = Label ( master, option, ... )
    # master − This represents the parent window.
import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 创建 Label 组件
label1 = tk.Label(root, text="你好，Tkinter!")

# 创建 StringVar 实例
var = tk.StringVar()
var.set("你好, StringVar")

label2= tk.Label(root, text="你好，Tkinter!",
                textvariable=var,
                 fg="red",
                 bg="green",
                underline= 5,
                 width=20,
                 font="Helvetica -20 bold italic",
                 relief="raised",
                 wraplength=100, # 可能是像素
                 justify=tk.LEFT)
# justify
    # Specifies how multiple lines of text will be aligned with respect to each other:
    # LEFT for flush left, CENTER for centered (the default), or RIGHT for right-justified.

# 将 Label 放置到窗口上
label1.pack()
label2.pack()

# 进入主事件循环
root.mainloop()