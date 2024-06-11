# 📚[7. Input and Output — Python 3.12.4 documentation](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
name = "John"
age = 25

print("Hello, {}!".format(name))

print("Hello, {}, {}!".format(name, age))

print("Hello, {name}, {age}!".format(name= "ali", age=19))

# 格式化字典和列表
print("{a} {b[0]}".format(a="Hello", b=["World", "There"]))

data = {"greeting": "Hello", "place": "World"}
print("{greeting}, {place}".format(**data))  # 輸出: Hello World

