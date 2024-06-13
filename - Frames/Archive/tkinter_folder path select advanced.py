import tkinter as tk
from tkinter import filedialog, messagebox

def button_select_click(text_var):
    path = filedialog.askdirectory(initialdir=r"C:\Users\daiyi\Desktop",
                                   title="選擇路徑",
                                   mustexist=True)
    text_var.set(path)

def initialize_ui(root):
    input_entry_text_var = tk.StringVar(value="輸入或選擇導入路徑")
    output_entry_text_var = tk.StringVar(value="輸入或選擇導出路徑")

    input_entry = tk.Entry(root, width=80, textvariable=input_entry_text_var)
    input_entry.grid(row=0, column=0)

    input_select_button = tk.Button(root, text="選擇導入路徑", command=lambda: button_select_click(input_entry_text_var))
    input_select_button.grid(row=0, column=1)

    output_entry = tk.Entry(root, width=80, textvariable=output_entry_text_var)
    output_entry.grid(row=8, column=0)

    output_select_button = tk.Button(root, text="選擇導出路徑", command=lambda: button_select_click(output_entry_text_var))
    output_select_button.grid(row=8, column=1)

    return input_entry, output_entry

def main():
    root = tk.Tk()
    root.title("Path Selector")
    root.geometry("600x200+400+200")

    input_entry, output_entry = initialize_ui(root)

    root.mainloop()

if __name__ == "__main__":

    main()