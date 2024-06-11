# 成员运算符用于判断一个值是否属于某个容器类型的元素，
#   比如列表（list）、元组（tuple）、字典的键（dict keys）、集合（set）或字符串（str）等。
# 🔢in：如果指定的值在容器中存在，则表达式返回 True，否则返回 False。
# 🔢not in：如果指定的值不在容器中，则表达式返回 True，否则返回 False。

# 列表示例
fruits = ['apple', 'banana', 'cherry']
if 'apple' in fruits:
    print("苹果在列表中")

# 字符串示例
text = "Hello, World!"
if 'World' in text:
    print("字符串中包含'World'")

# 集合示例
numbers = {1, 2, 3, 4, 5}
if 6 not in numbers:
    print("集合中不包含数字6")