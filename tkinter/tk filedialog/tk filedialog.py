# 🔢askopenfilename 选择单个文件
    # 打开一个文件对话框让用户选择一个文件，并返回所选文件的路径
# 🔢askopenfilenames 选择多个文件
    # 允许用户选择多个文件，返回一个包含所有选定文件路径的列表。
# 🔢asksaveasfilename 保存文件
    # 打开一个保存文件对话框让用户指定保存文件的位置和名称，返回文件路径。
# 🔢askdirectory 选择目录
    # 打开一个目录选择对话框，让用户选择一个目录，返回所选目录的路径
# 🔢askopenfile:
    # 类似于askopenfilename，但直接返回一个文件对象而不是文件路径

from tkinter import filedialog
# 🌰️askopenfilename 选择单个文件
def choose_file():
    # 打开文件选择对话框并获取用户选择的文件路径
    filepath = filedialog.askopenfilename()
    print("你选择了:", filepath)

# 假设你已创建了一个Tkinter窗口，这里直接调用choose_file函数
# choose_file()

# 🌰️askopenfilenames 选择多个文件
def choose_multiple_files():
    # 允许多选文件，返回文件路径列表
    filepaths = filedialog.askopenfilenames()
    print("你选择了多个文件:")
    for path in filepaths:
        print(path)

# choose_multiple_files()

# 🌰️asksaveasfilename 保存文件
def save_file():
    # 打开保存文件对话框，让用户指定保存位置和文件名
    filepath = filedialog.asksaveasfilename()
    print("文件将被保存到:", filepath)

# save_file()

# 🌰️askdirectory 选择目录
def choose_directory():
    # 打开目录选择对话框，让用户选择一个目录
    directory = filedialog.askdirectory()
    print("你选择了目录:", directory)

# choose_directory()