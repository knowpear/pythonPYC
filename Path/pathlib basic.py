from pathlib import Path

def get_user_home_directory():
    """
    🔢 Path.home() 获取用户家目录
    """
    home_dir = Path.home()
    print(f"用户家目录: {home_dir}")
    return home_dir

def print_parent_directory(path):
    """
    🔢 .parent 输出父目录
    """
    print(f"{path.name}的父目录: {path.parent}")

def print_file_name(path):
    """
    🔢 .name 输出文件名
    """
    print(f"{path}的文件名: {path.name}")

def check_file_existence(path):
    """
    🔢 .exists() 檢查文件是否存在
    """
    if path.exists():
        print(f"{path.name} exists")
    else:
        print(f"{path.name} does not exist")

def check_file_type(path):
    """
    🔢 .is_dir() 是否为目录
    🔢 .is_file() 检查是否为文件
    """
    if path.is_dir():
        print(f"{path.name} is a directory")
    elif path.is_file():
        print(f"{path.name} is a file")
    else:
        print(f"{path.name} is neither a file nor a directory")

def safe_open_file(path):
    """
    🔢 .open() 打开文件
    """
    try:
        with path.open() as file:
            content = file.read()
            print(f"文件內容: {content}")
    except Exception as e:
        print(f"无法打开文件 {path}：{e}")

def create_directory(path):
    """
    🔢 .mkdir() 创建目录
    """
    # parents = True: 如果需要的话，会创建所有不存在的上级目录
    # exist_ok = True: 如果目录已经存在，也不会抛出异常。
    try:
        path.mkdir(parents=True, exist_ok=True)
        print(f"目录 {path} 创建成功。") # 若已有內容, 不會覆蓋, 只會更新修改時間等

        (path / "empty").mkdir(exist_ok=True) # 🐾自創寫法. 待刪除的, 用於後續測試
        (path / "empty2").mkdir(exist_ok=True) # 待刪除的, 用於後續測試
    except Exception as e:
        print(f"无法创建目录 {path}：{e}")

def remove_empty_directory(path):
    """
    🔢 .rmdir() 删除空目录
    """
    # 🐾刪除自己本身, 而非sub folders
    try:
        (path / "empty").rmdir()
        (path / "empty2").rmdir()
        print(f"目录 {path} 已被删除。")
    except Exception as e:
        print(f"无法删除目录 {path}：{e}")

def touch_file(path):
    """
    🔢 .touch() 创建新文件
    """
    try:
        path.touch(exist_ok=True)
        print(f"文件 {path} 创建成功。")
    except Exception as e:
        print(f"无法创建文件 {path}：{e}")

def main():
    # 🔢 Path() 路徑字串創建
        # 使用对象来表示路径，允许链式调用方法，这让代码更加直观和易于理解。
    file_path = Path("./Layer root/pathlib file.txt")

    print_parent_directory(file_path)

    print_file_name(file_path)

    check_file_existence(file_path)

    check_file_type(file_path)

    safe_open_file(file_path)

    new_dir = Path("./Layer root/pathlib dir")

    create_directory(new_dir)

    # remove_empty_directory(new_dir)

    new_file = Path("Layer root/pathlib new_file.txt")

    touch_file(new_file)

if __name__ == "__main__":
    main()