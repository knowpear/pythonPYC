import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

var = tk.StringVar()
var.set("在此選擇路徑")

entry1 = tk.Entry(root, width=80, textvariable=var)
entry1.grid(row=0, column=0)

button1 = tk.Button(root, text="選擇路徑", command=lambda: var.set(filedialog.askdirectory()))
button1.grid(row=0, column=1)

root.mainloop()