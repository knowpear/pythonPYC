from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text = "Look, I clicked it!")
    myLabel.pack()

myButton = Button(root, text = "Click me!", command= myClick, fg = "blue", bg= "grey")
# 🔢command賦值的解釋
    # command = myClick是回調函數
    # 🧪command= lambda:myClick() 改成匿名函數亦可
    # 在Tkinter中，当您在按钮小部件中设置command参数时，您需要提供一个函数名，而不是函数的调用（即不带括号的函数）。
        # 这是因为您不是在定义按钮时调用该函数，而是告诉Tkinter：“当用户点击这个按钮时，请调用这个函数。”
        # 如果您写成command=myClick()，那么myClick函数将在按钮创建时立即执行，而不是在用户点击按钮时执行。这通常不是您想要的行为。

myButton.pack()

root.mainloop()