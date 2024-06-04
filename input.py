

def confirmation():
    while True:
        confirmation = input("请按下 Y 或 N 确认继续：")
        if confirmation.upper() == "Y":
            print("您选择了继续。")
            break
        elif confirmation.upper() == "N":
            print("您选择了取消。")
            break
        else:
            print("无效的输入。")
            continue

confirmation()