# 形參和實參
def pr(name): # 形參
    print(name)

man = "Siki" # 實參
pr(man)

# 🐾函數內參數
def add(a, b):
    res = a + b
    print(res)

add(5,6)

# 帶返回值函數
def multiply(a, b):
    res1 = a * b
    return res1
    # return a * b # 直接這樣寫也可
res2 = multiply(2, 3) # res2接收返回值; res1和res2也可以相同命名
print(res2)
# multiply(3, 5) # 返回值可以接收, 也可以不接收

# 可變個數參數
def test(a,*n): # 可變個數參數要放在參數列表最後一位
   for i in n:
       print(i)
test(1,2,3)