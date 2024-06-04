# 結束語
# end 参数定义了打印结束后的字符，默认为换行符 \n。
print("hello world", end="")
print("hello world")

# 多個參數
print("siki", "老師")
print("siki", "老師", sep='-')

# f-string
name = "Alice"
age = 18
print(f"Hello, {name}!")  # 使用 f-string

print(f'我的名字是{name}, 明年{age + 1}岁了')

print("Hello, {}!".format(name))  # 使用 .format() 方法

# string多行書寫, 換行輸出. 三個引號方法
print("""
aa
bb
cc
""")

# string 多行書寫, 單行輸出. \連續字符方法
print("dd\
ee\
ff\
gg") # 改成\n就成了換行了


# list多行定義
names = ["John", "Bob",
         "Mosh",
         "Sam", "Mary"]
print(names)

# dict多行定義
stu1 = {"age":17, "name":"siki",
        "gender":"男" }
print(stu1)