from tkinter import *

root = Tk()
root.title("tk initialization")
root.geometry("600x650")

def get_text():
    text = my_text.get(1.0, END)
    print(text)

def clear():
    my_text.delete(1.0, END)

my_text = Text(root, width=60, height=20, font=("Helvetica", 16))
my_text.pack(pady = 20)

button_frame = Frame(root)
button_frame.pack()

get_text_button = Button(button_frame, text= "Get text", command= get_text)
get_text_button.grid(row = 0, column = 0, padx = 20)

clear_button = Button(button_frame, text= "Clear screen", command=clear)
clear_button.grid(row = 0, column = 1)

root.mainloop()