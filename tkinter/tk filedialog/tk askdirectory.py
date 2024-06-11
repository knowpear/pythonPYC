import tkinter as tk
from tkinter import filedialog

def select_directory():
    root = tk.Tk()

    selected_directory = filedialog.askdirectory(
        initialdir="%USERPROFILE%/Desktop",  # 初始目录
        title="请选择一个文件夹",  # 对话框标题
        mustexist=True  # 只能选择存在的目录
    )

    if selected_directory:
        print(f"您选择的目录是: {selected_directory}")
    else:
        print("您未选择任何目录")

if __name__ == "__main__":
    select_directory()