# 📚[Built-in Functions — Python 3.12.4 documentation](https://docs.python.org/3/library/functions.html#print)
print("hello world")

# 多個參數
print("siki","老師")# 默認有空格. 当你使用逗号,分隔两个或多个字符串并传递给print函数时，print会默认在这些字符串之间添加一个空格
print("siki","老師", sep=" ") # 與此等價

print("siki" + "老師") # 默認沒空格

# 使用自定义分隔符连接两个字符串
print("siki", "老師", "好", sep='-')