# 📚[4. More Control Flow Tools — Python 3.12.4 documentation](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
# 🔢基本
# if 条件表达式:
#     # 当条件表达式为真（True）时执行的代码块

# 🔢選擇
# if 条件表达式1:
#     # 当条件表达式1为真时执行的代码块
# elif 条件表达式2:
#     # 当条件表达式1为假且条件表达式2为真时执行的代码块
# else:
#     # 当以上所有条件表达式都为假时执行的代码块

# 🔢嵌套
# if 条件表达式1:
#     # 当条件表达式1为真时
#     if 条件表达式2:
#         # 当条件表达式1和条件表达式2均为真时执行的代码块
#     else:
#         # 当条件表达式1为真但条件表达式2为假时执行的代码块
# else:
#     # 当条件表达式1为假时
#     if 条件表达式3:
#         # 当条件表达式1为假且条件表达式3为真时执行的代码块
#     else:
#         # 当条件表达式1和条件表达式3都为假时执行的代码块

temperature = 21
if temperature >30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a nice day.")
else:
    print("Not a valid day.")
print("done.")