numbers = ["1", "2", "3", "4", "5"]

print(len(numbers))

numbers.append("6")

numbers.insert(4, "new") # 預期下標, "object"
print(numbers)

print("3" in numbers) # 判斷, boolean result

numbers.clear()
print(numbers)
