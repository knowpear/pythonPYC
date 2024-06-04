from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.title("tk initialization")
root.geometry("400x400")

mylabel = Label(root, text = "hello world!")
mylabel.pack()


root.mainloop()