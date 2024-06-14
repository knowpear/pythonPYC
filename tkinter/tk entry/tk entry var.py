# 🔢var.get()
# 🔢var.set()

import tkinter as tk

root = tk.Tk()
root.title("tk initialization")
root.geometry("400x200+300+500")

entry1_text_var = tk.StringVar()
entry1_text_var.set("初始值")

entry1 = tk.Entry(root, width=30, textvariable=entry1_text_var)
entry1.pack()

root.mainloop()
