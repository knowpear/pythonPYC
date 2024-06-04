from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Q&A")

def take_input():
    input_text = input_text_widget.get("1.0", "end-1c")
    # 索引字符串 "1.0" 表示文本的起始位置。具体来说，它指的是第 1 行的第 0 列
    # "end"：索引字符串 "end" 表示文本框中最后一个字符之后的位置。它并不实际指向任何字符，而是指向文本末尾之后的位置。
    # "-1c"：表示从 "end" 位置向前移动一个字符。"c" 代表字符（character），-1c 表示往前一个字符。
    # "end-1c" 实际上指向最后一个字符。这避免了在获取文本时包含一个多余的换行符（因为 Text 小部件在内部会在结尾处添加一个不可见的换行符）。
    print(input_text)

# 創建 Text widget
input_text_widget = Text(root, height=8)
input_text_widget.pack()

# 按下按鈕後輸出文本
submit_button = Button(root, text="Submit", command=take_input)
submit_button.pack()

root.mainloop()