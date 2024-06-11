import tkinter as tk
root = tk.Tk()

n = 0

var = tk.StringVar()
var.set(str(n))

def myClick():
    global n
    n += 1
    var.set(str(n))
    myLabel.configure(textvariable=var)

myLabel = tk.Label(root, textvariable=var)
myLabel.pack()

myButton = tk.Button(root, text = "Click me!", command= myClick, fg = "blue", bg= "grey")


myButton.pack()

root.mainloop()