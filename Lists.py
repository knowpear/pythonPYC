
# 負數索引，Python會從列表的末尾開始倒數。因此，索引-1表示列表中的最後一個元素，索引-2表示倒數第二個元素，依此類推。
# 🔢
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Joh"
print(names[-1]) # 倒數第一個
print(names[-2]) # 倒數第二個
print(names[0:3]) # 開始下標:數量

# 🔢
numbers = ["1", "2", "3", "4", "5"]

print(len(numbers)) # 返回list長度

numbers.append("6")

numbers.insert(4, "new") # 預期下標, "object"
print(numbers)

print("3" in numbers) # 判斷, boolean result

numbers.clear()
print(numbers)