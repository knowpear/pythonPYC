
'''
**操作符在Python中用于解包字典，
它允许你将字典中的键值对作为关键字参数传递给函数。这意味着字典的每个键将成为函数的一个参数名，而对应的值则作为该参数的值。
简述 **data 语法
用途：在函数调用时，如果你有一个字典并且想用这个字典的键值对作为函数调用的参数，就可以使用**操作符。
示例：如果函数定义为func(a, b), 并且你有字典d = {'a': 1, 'b': 2}, 则调用func(**d)等同于调用func(a=1, b=2)。
限制：被调用的函数必须能够接受这些关键字参数，否则会引发错误。
文档说明或出处链接
Python官方文档对这一特性有详细的说明，你可以参考以下链接了解更多信息：
[4. More Control Flow Tools — Python 3.12.4 documentation](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
特别是关于可变参数的部分，其中提到了*args用于收集额外的位置参数，而**kwargs用于收集额外的关键字参数。
'''

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# 使用字典
person_data = {"name": "Alice", "age": 30}

# 在函数调用中使用**操作符展开字典为关键字参数
display_info(**person_data)