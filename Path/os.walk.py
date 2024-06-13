# 用于遍历目录树，生成目录树中文件夹路径、文件夹名称、文件名称的三元组。
# 📚[os — Miscellaneous operating system interfaces — Python 3.12.4 documentation](https://docs.python.org/3/library/os.html#os.walk)
'''
import os
for root, dirs, files in os.walk(top, topdown=True, onerror=None, followlinks=False):
    # 处理代码，例如打印每个文件的完整路径
    for name in files:
        print(os.path.join(root, name))
'''
# top：这是你想遍历的目录的路径，是os.walk()调用的必需参数。
# topdown：默认为True，决定遍历顺序。
    # 如果为True，则先遍历目录再遍历其子目录；
    # 如果为False，则先遍历子目录再遍历目录本身。
# onerror：如果在遍历过程中发生IO错误，此函数将被调用。默认值为None，表示忽略错误。
# followlinks：默认为False，如果设置为True，则会遍历符号链接指向的目录。

import os
path_root = r".\Layer root"

# 🔢遍历根目录及其子目录，打印每个目录的路径
for root, dirs, files in os.walk(path_root):
    print(f"当前root: {root}") # root是字符串, 不是集合

# 🔢遍历根目录及其子目录，打印每个子目录的名称和路径
for root, dirs, files in os.walk(path_root):
    # print(dirs) # 🧪dirs是各個層級文件夾的集合
    for dir_name in dirs:
        print(f"当前dir_name: {dir_name}")
        print(f"当前dir_name路径: {os.path.join(root, dir_name)}")

# 🔢遍历根目录及其子目录，打印每个文件的名称和路径
for root, dirs, files in os.walk(path_root):
    print(f"{files}") # 🧪files是各個層級文件的集合
    for file_name in files:
        print(f"当前files: {file_name}")
        print(f"当前files路径: {os.path.join(root, file_name)}")