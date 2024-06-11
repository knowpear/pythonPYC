# Syntax: global 变量名
x = 10  # 全局变量
def test_func():
    global x  # 声明x为全局变量
    x = x + 1  # 修改全局变量x的值

test_func()
print(x)  # 输出11，因为test_func内部修改了全局变量x

# 🐾先賦值, 再聲明