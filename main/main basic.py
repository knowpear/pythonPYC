# 📚[6. Modules — Python 3.12.4 documentation](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)
# 模块化：通过 if __name__ == "__main__": 结构，可以确保该模块既可以作为独立脚本运行，也可以被其他模块导入使用，而不会自动执行 main 函数中的代码。

def main():
    # 程序的主要逻辑
    print("Hello, World!")

if __name__ == "__main__":
    main()
# __name__ 是一个内置变量，当 Python 文件被直接运行时，其值为 "__main__"。
# 当文件被导入为模块时，其值为模块的名称。
# 这段代码确保 main 函数仅在脚本被直接运行时执行。