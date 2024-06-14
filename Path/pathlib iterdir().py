# 🔢.iterdir() 遍历目录下的所有条目，这包括文件和子目录
    # 🐾僅第一層級
from pathlib import Path

directory_path = Path('./Layer root')

# 🌰️遍歷所有文件夾和文件
def print_directory_contents(directory_path):
    # 确保路径存在且为目录
    if directory_path.is_dir(): # 🐾檢查要遍歷的根目錄的, 別混淆了
        # 使用.iterdir()方法遍历目录
        for entry in directory_path.iterdir():
            # 此表达式返回一个迭代器（Iterator），这个迭代器会产生目录中的条目（文件或子目录）的一个个Path对象。这意味着你可以通过循环（例如for循环）遍历这个目录下所有的条目。
            print(entry.name)
    else:
        print(f"路径 '{directory_path}' 不存在或不是一个目录。")

print_directory_contents(directory_path)

# 🌰️只遍歷所有文件夾
def print_directory_folders(directory_path):
    # 确保路径存在且为目录
    if directory_path.is_dir(): # 🐾檢查要遍歷的根目錄的, 別混淆了
        # 使用.iterdir()方法遍历目录
        for entry in directory_path.iterdir():
            # 打印每个条目的名称
            if entry.is_dir():
                print(entry.name)
    else:
        print(f"路径 '{directory_path}' 不存在或不是一个目录。")

print_directory_folders(directory_path)

# 🌰️只遍歷所有文件
def print_directory_files(directory_path):
    # 确保路径存在且为目录
    if directory_path.is_dir(): # 🐾檢查要遍歷的根目錄的, 別混淆了
        # 使用.iterdir()方法遍历目录
        for entry in directory_path.iterdir():
            # 打印每个条目的名称
            if entry.is_file():
                print(entry.name)
    else:
        print(f"路径 '{directory_path}' 不存在或不是一个目录。")

print_directory_files(directory_path)

# 🌰️遞歸遍歷所有文件(包括子文件夾)
def print_directory_files_recursive(directory_path):
    # 确保路径存在且为目录
    if directory_path.is_dir(): # 🐾檢查要遍歷的根目錄的, 別混淆了
        # 使用.iterdir()方法遍历目录
        for entry in directory_path.iterdir():
            # 打印每个条目的名称
            if entry.is_file():
                print(entry.name)
            else:
                print_directory_files_recursive(entry)
    else:
        print(f"路径 '{directory_path}' 不存在或不是一个目录。")

print_directory_files_recursive(directory_path)