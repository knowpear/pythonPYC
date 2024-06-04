try:
    a = 10
    b = 0 # 在0和其他之間調整b的值以供測試
    print(a/b)
    print('---') # 出現異常時, 這行不會被執行. 🐾逐行判斷
except ZeroDivisionError:
    # Code block that handles the exception
    print('代码出现异常了')
else:
    # Code block that executes if the try block *doesn't* raise an exception
    print('没有出现任何error')
finally:
    # Code block that always executes, whether an exception occurred or not
    pass
print('end')