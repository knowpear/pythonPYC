# 🔢var
    # var通常指的是与用户界面（UI）元素绑定的变量，用于控制或反映界面状态，如文本输入、复选框状态等。
    # Tkinter提供了几个专门的类来处理这类变量，它们分别是StringVar, IntVar, DoubleVar, 和 BooleanVar。
    # 这些变量类允许界面元素和Python程序之间的数据双向绑定，即界面的改变可以自动更新变量的值，反之亦然。

import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 创建一个StringVar实例
var = tk.StringVar()
var.set("初始值")

# 创建一个Label，并将其文本与my_var绑定
label = tk.Label(root, textvariable=var)
label.pack()

# 创建一个Entry，用户输入将与my_var同步
entry = tk.Entry(root, textvariable=var)
entry.pack()

root.mainloop()

print(var.get()) # 🐾取得關閉後的最終值