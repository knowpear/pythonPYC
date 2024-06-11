#📚[3. An Informal Introduction to Python — Python 3.12.4 documentation](https://docs.python.org/3/tutorial/introduction.html#variables-and-names)
# 标识符
# - 由数字、字母、下划线组成
# - 不能数字开头
# - 不能使用内置关键字
# - 严格区分大小写

# - 命名习惯
# 	- 见名知义。
# 	- 大驼峰：即每个单词首字母都大写，例如：`MyName`。
# 	- 小驼峰：第二个（含）以后的单词首字母大写，例如：`myName`。
# 	- 下划线：例如：`my_name`。

# 🔢type() 检测数据类型的方法

a = 1
print(type(a))  # <class 'int'> -- 整型

b = 1.1
print(type(b))  # <class 'float'> -- 浮点型

c = True
print(type(c))  # <class 'bool'> -- 布尔型

d = '12345'
print(type(d))  # <class 'str'> -- 字符串

e = [10, 20, 30]
print(type(e))  # <class 'list'> -- 列表

f = (10, 20, 30)
print(type(f))  # <class 'tuple'> -- 元组

h = {10, 20, 30}
print(type(h))  # <class 'set'> -- 集合

g = {'name': 'TOM', 'age': 20}
print(type(g))  # <class 'dict'> -- 字典
