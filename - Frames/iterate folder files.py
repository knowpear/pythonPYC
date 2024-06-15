from pathlib import Path
folder_path = Path('./- Samples/Layer root')
output_folder_path = Path('./- Samples/Layer root/output')

# Method1 - glob()
def iterate_folder_files1(input_path_root, output_path_root):
    for file in input_path_root.glob('*'):
        if file.is_file():
            print(file)
            # print(file.name)
            print('1 executable action')
iterate_folder_files1(folder_path, output_folder_path)

# Method2 - iterdir()
def iterate_folder_files2(input_path_root, output_path_root):
    for file in input_path_root.iterdir():
        if file.is_file():
            print(file)
            # print(file.name)
            print('2 executable action')

iterate_folder_files2(folder_path, output_folder_path)
