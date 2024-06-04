from tkinter import *


root = Tk()
root.title("tk initialization")

frame = LabelFrame(root, text= "This is my frame!", padx=50, pady=50)
frame.pack(padx=15, pady=15)

button = Button(frame, text= "Don't click here!")
button.grid(row = 0, column = 0)

button2 = Button(frame, text= "Don't click here!")
button2.grid(row = 1, column = 1)

root.mainloop()