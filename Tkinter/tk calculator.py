import tkinter
from tkinter import *

root = Tk()
root.title("simple calculator")

e = Entry(root, width= 35)
e.grid(row= 0, column = 0, columnspan = 3, padx = 10, pady = 10)
# columnspan specifies how many columns a widget will occupy. It allows a widget to stretch across multiple columns.

def button_click(number):
    # e.delete(0, END)
    # e.delete(0,tkinter.END)
    # END is a special Tkinter constant which refers to the position just after the last character in the widget.

    # 🔢🧑🏻‍🏫
    current = e.get()
    e.delete(0, END) # 清除重寫
    e.insert(0, str(current) + str(number))

    # 🔢🐾
    # current = e.get()
    # e.insert(len(current), str(number)) # 🐾✌️取當前長度→ 最末+1下標, 開始直接插入新數字
    return

def button_clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_num))

# define buttons
button_1 = Button(root, text="1", padx= 40, pady= 20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx= 40, pady= 20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx= 40, pady= 20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx= 40, pady= 20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx= 40, pady= 20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx= 40, pady= 20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx= 40, pady= 20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx= 40, pady= 20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx= 40, pady= 20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx= 40, pady= 20, command= lambda: button_click(0))
button_clear = Button(root, text="Clear", padx= 79, pady= 20, command= button_clear)
button_add = Button(root, text="+", padx= 39, pady= 20, command= button_add)
button_equal = Button(root, text="=", padx= 91, pady= 20, command= button_equal)
# padx: Represents the horizontal padding that adds space to the left and right of the widget.
# pady: Represents the vertical padding that adds space above or below the widget.

# put buttons on screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan = 2) # columnspan = 2 橫跨兩列
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)


root.mainloop()