# 🔢.glob()
# 🔢.rglob()
# Syntax: glob.glob(pathname, *, recursive=False)
    # pathname: 一个字符串或者字符串列表，包含shell通配符的路径名。
    # recursive: 可选参数，默认为False。如果设置为True，则会递归地搜索子目录。

from pathlib import Path
import glob
import os

directory_path = Path('./Layer root')

def find_txt_files1(directory_path):
    # 查找当前目录下所有以.txt结尾的文件
    # 注意：应将directory_path作为字符串处理并与通配符模式拼接
    txt_files = glob.glob(str(directory_path / '*.txt')) # 🔢寫法1
    print(txt_files) # 打印文件路径集合
    for txt_file in txt_files:
        print(txt_file) # 打印文件路径
        print(os.path.basename(txt_file))  # 提取文件名
find_txt_files1(directory_path)

def find_txt_files2(directory_path):
    """
    查找指定目录及其子目录下所有 .txt 文件。

    :param directory_path: Path 对象，表示要搜索的目录路径。
    """
    # 使用 pathlib 的 rglob 方法查找所有 .txt 文件
    for txt_file in directory_path.rglob('*.txt'): # 🔢寫法2
        yield txt_file  # 使用生成器返回找到的每个文件

# 遍历并处理找到的每个 .txt 文件
for txt_file in find_txt_files2(directory_path):
    print(f"Found file: {txt_file}")
