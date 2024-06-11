# 🔢config() 或 configure()
    # Syntax：label.config(option=value, ...)
    # 💡不能與time.sleep連用, 會不顯示窗口, 需要用Tkinter的.after方法📅2024-06-10

import tkinter as tk
root = tk.Tk()
def label_change(label_name):
    label_name.config(text='Goodbye World!')

label1 = tk.Label(root, text='Hello World!')
label1.pack()

# Use lambda to pass the label as an argument to label_change function after 2000 milliseconds
root.after(2000, lambda: label_change(label1))
# 📚GPT4.0 Using lambda, you can create an anonymous function that calls label_change with label1 as an argument, without executing it immediately. This ensures the function is called after the specified delay.

root.after(4000, lambda: label1.destroy()) # 🧪此處爲起始時間共同讀秒, 非延續時間
root.mainloop()

