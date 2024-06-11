numbers = list(range(10))
print(numbers)

numbers = list(range(1, 11))
print(numbers)

numbers = list(range(1, 10, 2))
print(numbers)

numbers = list(range(0, -10, -1))
print(numbers)

'''
tongyilingma
range(start, stop, step)
start（開始值，可選）: 序列生成的起始點，默認為0。
stop（停止值，必填）: 序列生成將在到達此值前停止，注意stop值本身不會被包括在序列中。
step（步長，可選）: 每次增值的大小，默認為1。
如果只提供一個參數，該參數將被視為stop值，並且start默認為0，step默認為1
📚[Built-in Types — Python 3.12.3 documentation](https://docs.python.org/3/library/stdtypes.html#ranges)
'''