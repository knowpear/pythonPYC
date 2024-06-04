stu1 = {"age":17, "name":"siki","gender":"男" }

# 遍歷鍵keys
print(stu1.keys())
for a in stu1.keys():
    print(a)

# 遍歷值values
print(stu1.values())
for b in stu1.values():
    print(b)

# 遍歷鍵值對items
print(stu1.items())
items = list(stu1.items())
for k,v in stu1.items():
   print(k,v)