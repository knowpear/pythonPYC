'''
在Tkinter库中，var通常指的是用来存储和管理界面元素状态的变量类，
🔢StringVar
🔢IntVar
🔢DoubleVar
🔢BooleanVar
这些变量类允许界面元素（如Entry, Label, Scale等）与其所显示的数据之间建立动态链接，使得数据变化时，界面能自动反映出这种变化，无需手动调用更新函数。

创建变量:
string_var = tkinter.StringVar()
int_var = tkinter.IntVar()
double_var = tkinter.DoubleVar()
bool_var = tkinter.BooleanVar()

设置变量值:
string_var.set("Hello, Tkinter!")
int_var.set(42)
double_var.set(3.14)
bool_var.set(True)

获取变量值:
value = string_var.get()
value = int_var.get()
value = double_var.get()
value = bool_var.get()
与界面元素绑定:
在创建界面元素时，使用textvariable, variable等属性与变量绑定。
'''
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("Tkinter StringVar 示例")

# 创建一个StringVar变量
text_var = tk.StringVar()
text_var.set("我是一个字符串变量。")

# 创建一个标签，其文本由StringVar控制
label = tk.Label(root, textvariable=text_var)
label.pack()  # 使用pack布局管理器放置标签

# 创建一个按钮，点击时設置text_var的值
button = tk.Button(root, text="点击我", command=lambda: text_var.set("按钮被点击了！"))
button.pack()

# 进入Tkinter事件循环
root.mainloop()
