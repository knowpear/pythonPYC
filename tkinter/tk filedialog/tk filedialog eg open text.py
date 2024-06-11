import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.filename = filedialog.askopenfilename(initialdir=r"G:\pCloud\python\pythonProject\Tkinter\tk files dialog box", title="Select a file", filetypes=(("txt files","*.txt"),("all files","*.*")))
def open_file():
    # Check if a file was selected
    if root.filename:
        my_label = tk.Label(root, text=root.filename).pack()
        os.startfile(root.filename)

my_btn = tk.Button(root, text="Open File", command= open_file).pack()

root.mainloop()