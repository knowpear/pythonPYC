import os
from tkinter import *
from tkinter import filedialog
# ⏳如果手工輸入路徑, 先讀取路徑?

root = Tk()
root.title("tk files dialog box")

# 创建一个文本框用于显示文件路径，初始时不显示任何文本
path_entry = Entry(root, width=50)
path_entry.pack()
def select_file():
    # 使用filedialog让用户选择文件
    global filepath
    filepath = filedialog.askopenfilename(
        initialdir=r"G:\pCloud\python\pythonProject\Tkinter\tk files dialog box",
        title="Select a file",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*"))
    ) # 🐾filepath應該是每次調用即時更新的
    # 如果选择了文件，则更新文本框内容并打开文件
    if filepath:
        path_entry.delete(0, END)  # 清空文本框
        path_entry.insert(0, filepath)  # 插入新的文件路径

def open_file():
    filepath = path_entry.get()
    os.startfile(filepath)  # 使用默认程序打开文件

# 创建一个按钮，当点击时会调用open_file函数
select_file_btn = Button(root, text="Select file", command=select_file)
select_file_btn.pack()
open_file_btn = Button(root, text="Open file", command=open_file)
open_file_btn.pack()

# 进入Tkinter事件循环
root.mainloop()