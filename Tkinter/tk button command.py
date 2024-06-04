from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text = "Look, I clicked it!")
    myLabel.pack()

# foreground color (text color)
myButton = Button(root, text = "Click me!", command= myClick, fg = "blue", bg= "grey")

# myButton.grid(row = 1, column = 1)
myButton.pack()

root.mainloop()