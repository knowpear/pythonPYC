
import tkinter as tk
def update_label():
    current_text = label.cget("text")
    new_text = "New Text" if current_text == "Original Text" else "Original Text"
    label.config(text=new_text)
    # 重新调度函数，形成循环
    root.after(2000, update_label)

root = tk.Tk()
label = tk.Label(root, text="Original Text")
label.pack()

update_label()  # 启动更新循环
root.mainloop()
