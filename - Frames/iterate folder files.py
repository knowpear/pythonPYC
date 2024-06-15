from pathlib import Path
foler_path = Path('../Path/Layer root')

# Method1 - glob()
def iterate_folder_files1(path_root):
    for file in path_root.glob('*'):
        if file.is_file():
            print(file)
            # print(file.name)
            print('1 executable action')
iterate_folder_files1(foler_path)

# Method2 - iterdir()
def iterate_folder_files2(path_root):
    for file in path_root.iterdir():
        if file.is_file():
            print(file)
            # print(file.name)
            print('2 executable action')

iterate_folder_files2(foler_path)
