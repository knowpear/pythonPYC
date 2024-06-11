import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def initialize_ui(root, text_var):
    entry1 = tk.Entry(root, width=80, textvariable=text_var)
    entry1.grid(row=0, column=0, padx=10, pady=10)

    button_select = tk.Button(root, text="選擇路徑", command=lambda: button_select_click(text_var))
    button_select.grid(row=0, column=1, padx=10)

    button_save = tk.Button(root, text="儲存路徑", command=lambda: button_save_click(entry1, text_var))
    button_save.grid(row=0, column=2, padx=10)

    return entry1

def button_select_click(text_var):
    path = filedialog.askdirectory(initialdir=r"C:\Users\daiyi\Desktop",
                                   title="選擇路徑",
                                   mustexist=True)
    if path:  # 如果路径不为空
        text_var.set(path)

def button_save_click(entry, text_var):
    saved_path = entry.get()
    messagebox.showinfo("提示", f"路徑已儲存: {saved_path}")

def main():
    root = tk.Tk()
    root.title("Path Selector")
    root.geometry("800x400+400+200")

    text_var = tk.StringVar(value="在此輸入或選擇路徑")

    initialize_ui(root, text_var)

    root.mainloop()

if __name__ == "__main__":
    main()