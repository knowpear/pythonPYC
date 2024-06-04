# 🔢傳統方式
my_file = open("game.txt", "r")
stuff = my_file.read()
print (stuff)
my_file.close()

# 🔢With方式
with open("game.txt", "r") as my_file:  # 使用with语句打开文件
    content = my_file.read()  # 读取文件内容
    print(content)  # 打印文件内容
# 文件在这里会自动关闭，不需要手动调用close()方法