import os
def iterate_folder_files_recursive(path_root):
    for item in os.listdir(path_root):
        item_path = os.path.join(path_root, item)
        if os.path.isdir(item_path):
            iterate_folder_files_recursive(item_path)
        else:
            print(item_path)

# 使用示例
path_root = r".\Layer root"
iterate_folder_files_recursive(path_root)
