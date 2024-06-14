# 🔢.glob()
# Syntax: Path.glob(pattern)
# 只會匹配當前目錄中的文件和目錄

# 🔢.rglob()
# Syntax: Path.rglob(pattern)
# 會遞歸地匹配當前目錄及其所有子目錄中的文件和目錄

# Expansion: Path.glob() 和 Path.rglob() 則是 pathlib 模塊的面向對象方法，直接操作 Path 對象，並且語法更加現代和直觀。
from pathlib import Path
import glob
import os

directory_path = Path('./Layer root')

def find_txt_files1(directory_path):
    # 查找当前目录下所有以.txt结尾的文件
    # 注意：应将directory_path作为字符串处理并与通配符模式拼接
    txt_files = directory_path.glob('*.txt')
    print(txt_files) # 打印文件路径集合
    for txt_file in txt_files:
        print(txt_file) # 打印文件路径
        print(f"1 Found file: {os.path.basename(txt_file)}")  # 提取文件名
find_txt_files1(directory_path)

def find_txt_files2(directory_path):
    """
    查找指定目录及其子目录下所有 .txt 文件。
    :param directory_path: Path 对象，表示要搜索的目录路径。
    """
    # 使用 pathlib 的 rglob 方法查找所有 .txt 文件
    for txt_file in directory_path.rglob('*.txt'):
        yield txt_file  # 使用生成器返回找到的每个文件

# 遍历并处理找到的每个 .txt 文件
for txt_file in find_txt_files2(directory_path):
    print(f"2 Found file: {os.path.basename(txt_file)}")