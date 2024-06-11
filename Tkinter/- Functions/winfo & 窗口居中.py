# 🔢root.winfo_screenwidth()
# 🔢root.winfo_screenheight()
from tkinter import *

def center_window(root, width=400, height=400):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (width/2))
    y_cordinate = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cordinate, y_cordinate))

root = Tk()
center_window(root)
root.title("Centered Main Window")

root.mainloop()