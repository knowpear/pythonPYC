
# 🔢逻辑与 (and): 当两边的操作数都为 True 时，整个表达式才为 True。
result = True and False  # 结果为 False
print(result)

# 🌰️使用逻辑与
age = 20
is_adult = age >= 18 and age < 65
print(is_adult)  # 输出 True

# 🔢逻辑或 (or): 当两边的操作数有一个为 True 时，整个表达式才为 True。
result = True or False  # 结果为 True
print(result)

# 🌰️使用逻辑或
login_attempt = 3
account_locked = login_attempt >= 5 or login_attempt < 0
print(account_locked)  # 输出 False

# 🔢逻辑非 (not): 将操作数的布尔值取反。
result = not True  # 结果为 False
print(result)

# 🌰️使用逻辑非
has_permission = True
cannot_access = not has_permission
print(cannot_access)  # 输出 False

price = 5
print(not price > 10) # result: True



