# 📚[Python3 运算符 | 菜鸟教程](https://www.runoob.com/python3/python3-basic-operators.html#ysf2)
# 🔢简单赋值运算符 (=): 用于将右边的值赋给左边的变量。
x = 5  # 将5赋值给x
# 🔢加法赋值运算符 (+=): 将变量的当前值加上一个数后，再赋值给该变量。
x += 3  # 相当于 x = x + 3
# 🔢减法赋值运算符 (-=): 将变量的当前值减去一个数后，再赋值给该变量。
x -= 3  # 相当于 x = x - 3
# 🔢乘法赋值运算符 (*=): 将变量的当前值乘以一个数后，再赋值给该变量。
x *= 3  # 相当于 x = x * 3
# 🔢除法赋值运算符 (/=): 将变量的当前值除以一个数后，再赋值给该变量。
x /= 3  # 相当于 x = x / 3
# 🔢取模赋值运算符 (%=): 将变量的当前值取模一个数后，再赋值给该变量。
x %= 3  # 相当于 x = x % 3
# 🔢整除赋值运算符 (//=): 将变量的当前值整除一个数后，再赋值给该变量。
x //= 3  # 相当于 x = x // 3
# 🔢乘方赋值运算符 (**=): 将变量的当前值乘以一个数后，再赋值给该变量。
x **= 3  # 相当于 x = x ** 3
# Assignment Expression 海象運算符
# 📚[6. Expressions — Python 3.12.4 documentation](https://docs.python.org/3/reference/expressions.html#assignment-expressions)
# 主要功能是在表达式内部进行赋值并立即返回赋值的结果
# 传统写法
n = 10
if n > 5:
    print(n)

# 使用海象运算符
if (n := 10) > 5:
    print(n)

if (n := len('fasffffsfsfsfsffsff')) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
