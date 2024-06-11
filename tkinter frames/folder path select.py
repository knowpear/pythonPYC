import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# 🐾思路是把操作都設置成var, 用的時候再讀取var
root = tk.Tk()
root.title("Path Selector")
root.geometry("800x400")
root.geometry("+400+200")

text_var = tk.StringVar()
text_var.set("在此輸入或選擇路徑")

def button_select_click():
    path = filedialog.askdirectory(initialdir=r"C:\Users\daiyi\Desktop",
                            title="選擇路徑",
                            mustexist=True)
    text_var.set(path)

def button_save_click():
    messagebox.showinfo("提示", f"路徑已儲存: {entry1.get()}")

def initialize_ui():
    entry = tk.Entry(root, width=80, textvariable=text_var)
    entry.grid(row=0, column=0)

    button_select = tk.Button(root, text="選擇路徑", command=lambda: button_select_click())
    button_select.grid(row=0, column=1)

    button_save = tk.Button(root, text="儲存路徑", command=lambda: button_save_click())
    button_save.grid(row=0, column=2)

    return entry

entry1 = initialize_ui()
# initialize_ui 函数返回 entry 对象，我们将它赋值给 entry1 变量。
# 现在，entry1 是在 root 代码块级别定义的，所以在 root.mainloop() 之前的任何地方都可以访问它。
# 🐾這裏是中介?

# 後續使用現用即可..
pathx = entry1.get()
print(pathx)

root.mainloop()