from tkinter import *
root = Tk()

myButton = Button(root, text = "button1")
myButton.grid(row = 1, column = 1)
myButton2 = Button(root, text = "button2", state= "disabled")
myButton2.grid(row = 2, column = 1)
myButton3 = Button(root, text = "button3", padx= 30, pady=10)
myButton3.grid(row = 4, column = 3)
root.mainloop()
