# 🔢after()
    # Syntax: widget.after(delay_ms, function_name, *args)
        # widget: 调用after()方法的Tkinter组件实例。
        # delay_ms: 以毫秒为单位的延迟时间，指定从现在起多少毫秒后执行函数。
        # function_name: 需要在延迟后调用的函数名称。
        # *args: 传递给function_name的额外参数，如果有多个参数，需要用逗号分隔。

import tkinter as tk
def change_text():
    # 更改label上的文字
    label1.config(text="时间到！")
    # 可以在这里添加更多操作或者调用其他函数

# 创建主窗口
root = tk.Tk()

label1 = tk.Label(root, text="演示標籤")
label1.pack()

# 使用after()方法，在2000毫秒 后调用change_text函数
root.after(2000, change_text)

# 启动Tkinter事件循环
root.mainloop()

