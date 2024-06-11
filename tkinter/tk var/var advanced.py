import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title("Path Selector")
root.geometry("600x400")
root.geometry("+400+200")

text_var = tk.StringVar()
text_var.set("在此輸入或選擇路徑")

def button_click():
    file_path = filedialog.askdirectory(initialdir="%USERPROFILE%/Desktop",
                            title="選擇路徑",
                            mustexist=True)
    # text_var.set(file_path) # part of Method2
    return file_path # part of Method3

entry1 = tk.Entry(root, width=80, textvariable=text_var)
entry1.grid(row=0, column=0)

# 🔢Method1 text_var直接設置接收filedialog參數
# button1 = tk.Button(root, text="選擇路徑", command=lambda: text_var.set(filedialog.askdirectory()))
# 🔢Method2 調用傳統事件函數, 函數體內設置text_var
# button1 = tk.Button(root, text="選擇路徑", command=button_click)
# ✌️🐾🔢Method3 text_var直接設置接收事件函數返回值
button1 = tk.Button(root, text="選擇路徑", command=lambda: text_var.set(button_click()))
button1.grid(row=0, column=1)

root.mainloop()