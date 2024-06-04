from tkinter import *

root = Tk()

e = Entry(root, width= 50, bg= "blue", fg= "white", borderwidth=5)
# 預設文本
e.insert(0, "Enter your name:")
# e.insert(6, "abc") # 第一个参数是插入文本的位置
e.pack()

def myClick():
    myLabel = Label(root, text = "hello, " + e.get())
    myLabel.pack()
myButton = Button(root, text = "Click me!", command= myClick, fg = "blue", bg= "grey")
myButton.pack()

root.mainloop()