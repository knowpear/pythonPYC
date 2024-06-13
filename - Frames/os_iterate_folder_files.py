import os
def iterate_folder_files(path_root):
    for root, dirs, files in os.walk(path_root):
        for file in files:
            print(os.path.join(root, file))

path_root = r"../Path/Layer root"
iterate_folder_files(path_root)