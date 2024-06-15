

from pathlib import Path
# 🔢.suffix 获取文件的基本后缀（包含点）
file_path = Path("./Layer root/pathlib file.txt")
print(file_path.suffix)

# 🔢.suffixes 获取文件的所有后缀列表，这是一个包含所有后缀（每个后缀前都有一个点）的列表
multi_ext_file = Path("./Layer root/Layer root.txt.md")
print(multi_ext_file.suffixes) # 輸出['.txt', '.md']

# 🔢with_suffix
# 用于改变或添加文件路径的后缀
    # Syntax: new_path = path.with_suffix(new_suffix)
    # new_suffix: 字符串类型
# 创建一个Path对象代表基础文件名
base_path = Path("报告.docx")

# 使用with_suffix方法来改变或添加后缀
full_path_with_suffix = base_path.with_suffix(".pdf")

print(full_path_with_suffix)  # 应输出: 报告.pdf