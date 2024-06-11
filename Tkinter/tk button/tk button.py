#
# Syntax: tk.Button(master, options...)
    # master: 父容器，即按钮所在的窗口或框架等。
    # options: 一系列键值对参数，用于定义按钮的外观和行为。常用选项包括但不限于：
    # text: 按钮上显示的文本。
    # command: 指定当按钮被点击时调用的函数。
    # fg 或 foreground: 按钮文本的颜色。
    # bg 或 background: 按钮背景色。
    # font: 按钮文本的字体样式。
    # width, height: 按钮的宽度和高度。
    # state: 按钮的状态，可以是 "normal"（默认，可点击）、"active"（被激活时的状态）、"disabled"（不可点击）。
    # padx, pady: 文本周围的水平和垂直填充空间。
    # relief: 按钮边缘样式，如 "flat", "groove", "raised", "ridge", "solid", "sunken"。

import tkinter as tk
root = tk.Tk()

myButton = tk.Button(root, text = "button1")
myButton.grid(row = 1, column = 1)

myButton2 = tk.Button(root, text = "button2", state= "disabled")
myButton2.grid(row = 2, column = 1)

myButton3 = tk.Button(root, text = "button3", padx= 30, pady=10)
myButton3.grid(row = 4, column = 3)

root.mainloop()
