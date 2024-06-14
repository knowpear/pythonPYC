from pathlib import Path
# 🔢拼接路径
'''
path = Path("documents") / "projects" / "report.txt"
print(path)  # 输出: documents/projects/report.txt
'''

# 🔢.joinpath()

# 🌰️1
path = Path("documents")
path = path.joinpath("projects")
path = path.joinpath("report.txt")
print(path)  # 输出: documents/projects/report.txt

# 🌰️2
base_dir = Path("documents")
subdir = "projects"
filename = "report.txt"

full_path = base_dir.joinpath(subdir, filename)
print(full_path)  # 输出: documents/projects/report.txt

# 🌰️3
p = Path("C:/")
folder = "downloads"
file_type = "images"
specific_file = "vacation.jpg"

# 混合使用字符串与变量构建路径
path = p.joinpath(folder, file_type, specific_file)

print(path)  # 输出类似于: /Users/YourUsername/downloads/images/vacation.jpg