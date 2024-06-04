# 打印星星
i = 0
while i <= 3:
    print(i * "*") # python可以連接數字和字符, 表示單位數量的字符
    i = i + 1

# 嵌套if
j = 0
while j <= 3:
    print(j) # python可以連接數字和字符, 表示單位數量的字符
    if j == 2: # 這裏注意是等價而非賦值
        break
    j = j + 1

# while 嵌套
k = 0
while k <= 5:
    print(k)
    while k <=2:
        print("小於2啦")
        k += 1
    k += 1