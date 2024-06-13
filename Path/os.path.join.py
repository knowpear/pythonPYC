# Syntax: os.path.join(path1[, path2[, ...]])
    # path1, path2, ...：表示要连接的路径组件，可以是字符串。这些组件会被正确地连接起来，形成一个合法的文件或目录路径。
    # 自動添加連接符, 根據操作系統
import os

# 定义根目录路径，使用原始字符串避免路径中的反斜杠转义
path_root = r".\Layer root"

# 列出根目录下的所有文件和子目录
sub_files = os.listdir(path_root)

# 打印根目录下的文件和子目录列表
print(sub_files)

# 遍历根目录下的所有文件和子目录
for file in sub_files:
    # 拼接完整文件路径并打印
    print(os.path.join(path_root, file))
