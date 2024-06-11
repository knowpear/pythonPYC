import tkinter as tk
from tkinter import filedialog

root = tk.Tk()  # 创建Tkinter窗口实例，通常隐藏起来作为对话框的父窗口
def select_file_with_options():

    # 使用askopenfilename方法，并设置多种属性
    file_path = filedialog.askopenfilename(
        title="选择图片文件",  # 自定义对话框标题
        # initialdir="~/Pictures",  # 初始目录设置为图片目录
        initialdir="%USERPROFILE%/Desktop",  # 初始目录设置为图片目录
        filetypes=[("图片文件", "*.jpg;*.png"), ("所有文件", "*.*")],  # 限制选择图片文件类型
        multiple=False,  # 允许多选文件 🐾若爲True, 結果爲元祖, 需要遍歷了
        parent=root,  # 指定父窗口，对于某些窗口管理器可能会影响对话框位置
        # 注意：以下属性并非所有Tkinter版本或平台都支持
        # initialfile="example.jpg",  # 初始选中的文件名
        # defaultextension=".jpg",  # 如果用户输入文件名不包含扩展名，则自动添加此扩展
    )

    # if file_path:  # 检查用户是否选择了文件
    #     print("你选择的文件路径是:", file_path)
    # else:
    #     print("未选择任何文件。")
    return file_path

x = select_file_with_options()
print(x)