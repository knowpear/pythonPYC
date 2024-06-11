# Syntax: (expression for item in iterable if condition)
# 🐾(expression + for item in iterable + if condition) 三部分組成
# 📚[6. Expressions — Python 3.12.3 documentation](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-generator_expression)

# 创建一个列表
numbers = [1, 2, 3, 4, 5]

# 使用生成器表达式计算所有偶数的平方
even_squares = (x ** 2 for x in numbers if x % 2 == 0)

# 迭代生成器对象并打印每个偶数的平方值
for square in even_squares:
    print(square)
