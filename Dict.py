# 創建空字典
stu1 = {}
# 創建字典
stu1 = {"age":17, "name":"siki","gender":"男" }
# 打印值
print(stu1["age"])
print(stu1["name"])
print(stu1["gender"])
# 添加鍵值對
stu1["rank"] = 3
print(stu1["rank"])
# 修改鍵值對
stu1["age"] = 18
print(stu1["age"])
# 刪除鍵值對
del(stu1["age"])
del stu1["name"]
print(stu1)

stu1 = {"age":17, "name":"siki",
        "gender":"男" }
print(stu1)

# list嵌套dict
students = [ { "name":"siki","age":17,"gender":"男" },
             { "name":"lichen","age":27,"gender":"女" },
             { "name":"siki","age":17,"gender":"男" },
             { "name":"siki","age":17,"gender":"男" }]
print(students[1]["name"])

# dict嵌套list
stu1 = { "name":"siki","age":17,"gender":"男","hobby":["篮球","足球","画画"] }
print(stu1["hobby"][1])