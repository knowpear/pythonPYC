import tkinter as tk
def update_counter(count):
    """更新标签上的计数值，并重新调度自身以实现连续计数"""
    label.config(text=count)
    # 递增计数，并在1000毫秒后再次调用update_counter，传递新的计数值
    root.after(1000, update_counter, count + 1)

# 创建主窗口
root = tk.Tk()

# 初始化计数器
count = 0

# 创建一个标签来显示计数
label = tk.Label(root, text=0)
label.pack()

# 啓用內循環
update_counter(count)

# 运行Tkinter事件循环
root.mainloop()
