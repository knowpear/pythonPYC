
# 身份运算符在编程语言中用于比较两个对象的引用或者内存地址，判断它们是否是同一个对象实例。
# is：如果两个变量引用的是内存中的同一个对象，则表达式返回 True，否则返回 False。这涉及到对象的唯一性，而非值的相等性。
# is not：与 is 运算符相反，如果两个变量引用的不是同一个对象，则表达式返回 True，如果它们引用相同对象则返回 False。
a = [1, 2, 3]
b = a  # b 指向与 a 同一个列表对象
c = [1, 2, 3]  # c 是一个新列表，内容与 a 相同，但不是同一个对象

print(a is b)  # 输出 True，因为 a 和 b 引用同一个对象
print(a is c)  # 输出 False，虽然内容相同，但是两个不同的对象
print(a == c)  # 输出 True，因为 a 和 c 的内容相等
