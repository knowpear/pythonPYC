import os
# print(os.getcwd())
os.startfile("game.txt")

# 讀取整個文件
def readtotal():
    with open("game.txt", "r",) as file:
        content = file.read()
        print(content)
readtotal()

# 逐行讀取
def readline():
    with open("game.txt") as file:
        for lines in file:
            # print(lines)
            # print(lines.rstrip())
            print(lines.rstrip('\n'))
# readline()

# 首行逐字讀取
def words_in_single_line():
    with open("game.txt") as file:
        single_line = file.readline()
        for words in single_line:
            print(words.rstrip())
# words_in_single_line()

# 全文逐字(詞)輸出
def words_in_total():
    with open("game.txt") as file:
        for lines in file:
            for words in lines:
            # for words in lines.split(): # 分隔每一行單詞並輸出 Split the content by any whitespace to get individual words
                print(words.rstrip())
# words_in_total()

# 附加寫入
# with open("game.txt", "a") as file:
#     file.write("\nwww.sikiedu.com") # 換行輸出

