# expectation
'''
*
**
***
****
*****
'''

# 一行输出星星的个数和行号是相等的
j = 1 # 行號
while j <= 5: # 外層控制行數
    i = 1 # i每次換行都要重新計數
    while i <= j: # 內層控制行內**數量
        print("*", end="")
        i += 1
    print(end = "\n") # 換行 equal to print(end = "") equal to print()
    j += 1 # 行號每次遞增1