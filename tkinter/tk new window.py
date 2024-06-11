from tkinter import *

root = Tk()
root.title("tk initialization")
root.geometry("400x400")

def open():
    top = Toplevel()
    top.title("top titile")

    mylabel = Label(top, text = "hello world!")
    mylabel.pack()

    button2 = Button(top, text= "close window", command= top.destroy).pack()

button = Button(root, text="Show new button", command=open)
button.pack()

root.mainloop()