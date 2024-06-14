import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("main window")
        master.geometry("400x400+500+200")
        self.create_widgets()

    def create_widgets(self):
        # 这里可以添加更多的控件和布局管理代码
        pass

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainWindow(root)
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        # 可以在这里添加更多的错误处理逻辑，比如显示错误对话框，或者记录错误日志
