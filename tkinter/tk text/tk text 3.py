from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("800x600")
root.title("Q&A")

def open_txt():
    txt_file = filedialog.askopenfilename(
        # initialdir= r"G:\pCloud\python\pythonProject\Tkinter\tk text",
        initialdir= ".",
        title= "Select a file",
        filetypes= (("txt files", "*.txt"), ("all files", "*.*"))
    )
    txt_file = open(txt_file, 'r')
    stuff = txt_file.read()
    # my_text.insert(END, stuff)
    my_text.insert(1.0, stuff) # text_widget.insert(index, text)
    txt_file.close()

def save_txt():
    saved_file = filedialog.askopenfilename(
        # initialdir= r"G:\pCloud\python\pythonProject\Tkinter\tk text",
        initialdir= ".",
        title= "Select a file",
        filetypes= (("txt files", "*.txt"), ("all files", "*.*"))
    )
    saved_file = open(saved_file, 'w')
    saved_file.write(my_text.get(1.0, END))

my_text= Text(root, width= 40, height= 10, font=("Helvetica", 16))
my_text.pack(pady=20)

open_button = Button(root, text= "Open this file", command=open_txt)
open_button.pack(pady = 20)
save_button = Button(root, text= "Save this file", command=save_txt)
save_button.pack(pady = 20)

root.mainloop()