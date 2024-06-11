# 判斷是否為奇數
print("常規判斷是否為奇數: ")
l = [2, 4, 7]
for num in l:
    if num % 2 != 0:
        print(True)
    else:
        print(False)

# 使用lambda判斷是否為奇數
print("使用lambda判斷是否為奇數: ")
l = [2, 4, 7]
for i in l:
    # your code here
    my_lambda = lambda x : x % 2 != 0
    # my_lambda = lambda x : (x % 2) != 0 # 這裏也可以加括號
    print(my_lambda(i))

# Lambda with multi results
print("Lambda with multi results: ")
l = [2, 4, 7]
jud_lambda = lambda x: (i % 2 != 0 for i in x)

for result in jud_lambda(l):
    print(result)