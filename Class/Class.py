class Dog():
    # __init__ 初始化函數; 構造函數
    def __init__(self, name, age, color):
        self.name = name # 前面name是屬性名, 後面name是屬性值
        self.age = age
        self.color = color

    def sit(self):
        print(self.name + "我坐下來了")

    def roll_over(self):
        print(self.name + "我正在打滾")

# 實例
# 對象名 也是一個變量名
# __init__可省略是因爲初始化函數會被自動調用
dog1 = Dog("大白", 2, "黑色")
dog2 = Dog("小小", 3, "黑白")

print(dog1.name)
print(dog2.name)

dog1.sit()
dog2.sit()