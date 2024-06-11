
# syntax: input([prompt])
# prompt是一個可選參數，用於指定在請求用戶輸入之前顯示的消息或提示。
    # 如果不提供此參數，則不會顯示任何提示，直接等待用戶輸入。
input()

name = input("請輸入您的名字：")
print("歡迎您，" + name + "!")

# 默認爲字符串類型