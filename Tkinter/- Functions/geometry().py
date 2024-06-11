'''
Tkinter库中的geometry方法用于设置或更改Tkinter窗口的大小和位置。这个方法接受一个字符串参数，
syntax: "{width}x{height}+{x_offset}+{y_offset}"，
    {width} 和 {height} 分别指定了窗口的宽度和高度（以像素为单位）。
    {x_offset} 和 {y_offset} 指定了窗口左上角在屏幕上的水平和垂直偏移量。
例如，root.geometry("400x400+100+100")会创建一个宽高均为400像素，并且位于屏幕坐标(100, 100)处开始的窗口。
关于Tkinter的官方文档是一个很好的参考来源，但请注意Tkinter是Tk GUI工具包的Python接口，其底层文档通常是Tk的文档。对于geometry方法的具体说明，虽然直接的Python官方文档链接可能不易找到详细说明，Tkinter遵循Tk的API，你可以在Tk文档中找到相应信息。不过，Python的Tkinter模块的文档通常随Python安装提供，在线文档资源如Python官方文档网站也会有概述性质的介绍
# 📚[Geometry Method in Python Tkinter - GeeksforGeeks](https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/)
'''

from tkinter import *

root = Tk()
root.title("main window")
root.geometry("400x400+800+200") # ❗中間不能有空格

root.mainloop()