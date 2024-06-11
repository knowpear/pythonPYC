from tkinter import *
root = Tk()
label1 = Label(root, text = "1st text")
label2 = Label(root, text = "2nd text")
label3 = Label(root, text = "3rd text").grid(row = 4, column = 5)

label1.grid(row = 0, column = 0, padx = (30,15))
# padx=10: 在小部件的左右两侧各增加10个像素的填充。
# padx=(10, 20): 在小部件的左侧增加10个像素的填充，在右侧增加20个像素的填充。
label2.grid(row = 3, column = 5, pady = (0,50))
# pady=10: 在小部件的上下两侧各增加10个像素的填充。
# pady=(10, 20): 在小部件的上方增加10个像素的填充，在下方增加20个像素的填充。
root.mainloop()