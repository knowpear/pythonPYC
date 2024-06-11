'''
当你使用 from tkinter import * 导入时，
    Tkinter库中的所有公共成员（包括Tk类）都被直接导入到了当前的命名空间，因此可以直接使用 Tk() 来创建主窗口对象，如 root = Tk()。
而当你使用 import tkinter as tk 导入时，
    你是通过tk这个别名来访问Tkinter库中的所有内容。因此，你需要使用 tk.Tk() 来创建主窗口对象，即 root = tk.Tk()。
'''
# 🔢Method1
import tkinter as tk
# 创建主窗口
root = tk.Tk()

# 🔢Method2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
root = Tk()

# root.title("tk initialization")
# root.geometry("400x400")
#
# mylabel = Label(root, text = "hello world!")
# mylabel.pack()
#
# root.mainloop()