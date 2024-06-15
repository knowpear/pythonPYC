import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# 🐾思路是把操作都設置成var, 用的時候再讀取var
from pathlib import Path

root = tk.Tk()
root.title("tkinter_folder path select")
root.geometry("600x200")
root.geometry("+400+200")

# 分別定義tk文本變量
# 輸入框文本變量
input_entry_text_var = tk.StringVar()
input_entry_text_var.set("輸入或選擇導入路徑")
# 輸出框文本變量
output_entry_text_var = tk.StringVar()
output_entry_text_var.set("輸入或選擇導出路徑")

# 共用點擊事件傳參改參→ 設置文本框
def button_select_click(text_var):
    # text_var是形參, 傳入哪個entry的var, 就更改哪個entry框內的值
    path = filedialog.askdirectory(initialdir=r"C:\Users\daiyi\Desktop",
                                   title="選擇路徑",
                                   mustexist=True)
    text_var.set(path)

# 執行程序→ 參數即時獲取即可
def get_current_path():
    # input_path = input_entry.get()
    # output_path = output_entry.get()
    # 上下這兩種都可以
    input_path = Path(input_entry_text_var.get())  # 這裏轉化爲pathlib.Path類型
    output_path = Path(output_entry_text_var.get())
    # print(f"導入路徑: {input_path}, 導出路徑: {output_path}")
    return input_path, output_path  # 返回輸入輸出路徑以復用

def iterate_folder_files1(input_path_root, output_path_root):
    for file in input_path_root.glob('*'):
        if file.is_file():
            print(file)
            # print(file.name)
            print('iterate_folder_files1 execute')

# 初始化UI
def initialize_ui(root):
    # 導入路徑框
    input_entry = tk.Entry(root, width=80, textvariable=input_entry_text_var)
    input_entry.grid(row=0, column=0)

    # 選擇導入按鈕
    input_select_button = tk.Button(root, text="選擇導入路徑",
                                    command=lambda: button_select_click(input_entry_text_var))
    input_select_button.grid(row=0, column=1)

    # 導出路徑框
    output_entry = tk.Entry(root, width=80, textvariable=output_entry_text_var)
    output_entry.grid(row=8, column=0)

    # 選擇導出按鈕
    output_select_button = tk.Button(root, text="選擇導出路徑",
                                     command=lambda: button_select_click(output_entry_text_var))
    output_select_button.grid(row=8, column=1)

    # 執行按鈕
    execute_button = tk.Button(root, text="執行", command=lambda: iterate_folder_files1(*get_current_path())) # 主體用執行程序, 接收傳參函數返回值
    execute_button.grid(row=10, column=0)

    return input_entry, output_entry

input_entry, output_entry = initialize_ui(root)
# initialize_ui 函数返回 輸入輸出兩個entry 对象，我们将它赋值给input_entry, output_entry变量。🐾可異名接收, 實例化?
# 现在，entry1 是在 root 代码块级别定义的，所以在 root.mainloop() 之前的任何地方都可以访问它。

root.mainloop()
