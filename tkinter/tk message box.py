from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("tk initialization")
root.geometry("400x400")

def popup():
    # messagebox.showinfo("This is my Popup!", "hello world")
    # messagebox.showwarning("This is my Popup!", "hello world")
    # messagebox.showerror("This is my Popup!", "hello world")
    # messagebox.askquestion("This is my Popup!", "hello world")
    # messagebox.askokcancel("This is my Popup!", "hello world")
    response = messagebox.askyesno("This is my Popup!", "hello world")
    my_label = Label(root, text=response) # yes = 1, no = 0 # 如果同行會報錯, The my_label variable is not being assigned the label widget because .pack() method is called on the same line, which returns None.
    my_label.pack()
    if response == 1:
        my_label.config(text="You clicked yes!")
    else:
        my_label.config(text="You clicked no!")

button = Button(root, text= "Popup", command= popup).pack()


root.mainloop()