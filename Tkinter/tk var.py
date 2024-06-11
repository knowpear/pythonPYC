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