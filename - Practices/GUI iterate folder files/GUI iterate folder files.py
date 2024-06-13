import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# 🐾思路是把操作都設置成var, 用的時候再讀取var
import os
from PIL import Image
from pathlib import Path

root = tk.Tk()
root.title("Path Selector")
root.geometry("600x200")
root.geometry("+400+200")

# 分別定義tk文本變量
# 輸入框文本變量
input_entry_text_var = tk.StringVar()
input_entry_text_var.set("輸入或選擇導入路徑")
# 輸出框文本變量
output_entry_text_var = tk.StringVar()
output_entry_text_var.set("輸入或選擇導出路徑")

# 共用點擊事件
def button_select_click(text_var):
    # text_var是形參, 傳入哪個entry的var, 就更改哪個entry框內的值
    path = filedialog.askdirectory(initialdir=r"C:\Users\daiyi\Desktop",
                            title="選擇路徑",
                            mustexist=True)
    text_var.set(path)

def initialize_ui(root):
    # 導入路徑框
    input_entry = tk.Entry(root, width=80, textvariable=input_entry_text_var)
    input_entry.grid(row=0, column=0)

    # 選擇導入按鈕
    input_select_button = tk.Button(root, text="選擇導入路徑", command=lambda: button_select_click(input_entry_text_var))
    input_select_button.grid(row=0, column=1)

    # 導出路徑框
    output_entry = tk.Entry(root, width=80, textvariable=output_entry_text_var)
    output_entry.grid(row=8, column=0)

    # 選擇導出按鈕
    output_select_button = tk.Button(root, text="選擇導出路徑", command=lambda: button_select_click(output_entry_text_var))
    output_select_button.grid(row=8, column=1)

    return input_entry, output_entry

input_entry, output_entry = initialize_ui(root)
# initialize_ui 函数返回 輸入輸出兩個entry 对象，我们将它赋值给input_entry, output_entry变量。🐾可異名接收, 實例化?
# 现在，entry1 是在 root 代码块级别定义的，所以在 root.mainloop() 之前的任何地方都可以访问它。

# 获取路径的函数应该在需要时调用，而不是直接在这里赋值
def get_paths():
    # 定義輸入路徑 = 輸入框路徑 = 要遍歷的路徑
    path_root = input_entry.get() # 🐾寫法
    # path_root = input_entry_text_var.get() # AI寫法
    # 定義輸出路徑 = 輸出框路徑 = 要導出的路徑
    output_path = output_entry.get() # 🐾寫法
    # output_path = output_entry_text_var.get() # AI寫法
    return path_root, output_path

def resize_image(image_path, output_image_path):
    # 目标尺寸
    width, height = 600, 600  # 举例，您可以根据需要设置
    with Image.open(image_path) as img:
        # 调整图片尺寸
        resized_img = img.resize((width, height), Image.LANCZOS)
        # 保存调整尺寸后的图片
        resized_img.save(output_image_path, optimize=True,
                         quality=85)  # optimize=True, quality=85是從網上抄得的, 不知道有沒有用
        print(f"图片 {image_path} 处理成功")

def iterate_folder_files(path_root, output_path):
    for root, dirs, files in os.walk(path_root):
        for file in files:
            input_file_path = os.path.join(root, file)
            # input_file_path = os.path.join(path_root, file) # ❌🧪若無子目錄, 則平安無事, 若有, 則選定目錄不符合於os.walk遍歷的所有子目錄規則, 找不到會報錯
            output_file_path = os.path.join(output_path, file)
            resize_image(input_file_path, output_file_path)

# 執行按鈕
excute_button = tk.Button(root, text="執行", command=lambda: iterate_folder_files(*get_paths()))
excute_button.grid(row=10, column=0)

root.mainloop()