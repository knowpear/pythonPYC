numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

str1 = "python"
for i in str1:
    if i == "t":
        print("不打印")
        continue # 跳過循環剩餘部分並繼續
        # break # 跳出該循環
    print(i)