# 假设有效输入定义为常量，以提高代码的可维护性
VALID_INPUTS = {"Y", "N"}

CONFIRM_CONTINUE = "Please press Y or N to confirm continuation:"
INVALID_INPUT = "Invalid input."

def confirmation():
    attempt = 0
    attempt_limit = 5  # /为了防止无限循环，设置尝试次数上限
    while True:
        confirmation = input(CONFIRM_CONTINUE).upper()
        if confirmation in VALID_INPUTS:
            if confirmation == "Y":
                print("You chose to continue.")
            else:  # confirmation == "N"
                print("You chose to cancel.")
            break
        else:
            print(INVALID_INPUT)
            if attempt < attempt_limit - 1:  # 未达到尝试次数上限，继续循环
                attempt += 1
                continue
            else:
                # 达到尝试次数上限，给出警告并结束循环
                print("You have reached the maximum number of attempts.")
                break

confirmation()
