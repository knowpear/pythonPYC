# Syntax: os.listdir(path='.')
    # 列出指定目錄中的所有檔案和目錄
    # path：一个字符串对象，表示要列出其内容的目录的路径。默认值为 '.'，表示当前工作目录
    # 不遞歸
# 📚[os — Miscellaneous operating system interfaces — Python 3.12.4 documentation](https://docs.python.org/3/library/os.html#os.listdir)

import os
path = "./Layer root"
content = os.listdir(path)

print(content)

for i in content:
    print(i)