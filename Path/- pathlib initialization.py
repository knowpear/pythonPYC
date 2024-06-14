# 面向对象接口：pathlib 使用对象来表示路径，允许链式调用方法，这让代码更加直观和易于理解。例如，你可以像这样操作路径：path = Path('dir').joinpath('subdir', 'file.txt')。
# 更好的可读性：使用 / 操作符来连接路径，使得代码看起来更像自然语言，例如 path = Path('dir') / 'subdir' / 'file.txt'，这在处理多级目录时特别有用。
# 跨平台兼容性：pathlib 自动处理不同操作系统间的路径分隔符，使得代码无需关心运行环境是Windows、Linux还是macOS。
# 丰富的方法集：提供了许多实用方法，如检查路径是否存在(exists()), 创建目录(mkdir()), 获取父目录(parent)，读写文件(open())等，这些都直接集成在路径对象中。

