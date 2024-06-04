# 使用了with语句来确保文件在使用后正确地关闭。
# readline()被用来读取文件中的第一行，然后进入一个循环，
# 在循环中继续调用readline()读取后续的行，直到读取到空字符串，表示到达文件末尾
with open("./game.txt", "r", encoding="GBK") as file:
    # 逐行读取
    line = file.readline()
    while line:
        # 处理每一行
        print(line, end='')  # end='' 避免打印额外的换行符
        line = file.readline()  # 读取下一行


with open('./game.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")