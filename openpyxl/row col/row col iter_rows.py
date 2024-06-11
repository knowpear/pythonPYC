import openpyxl
wb = openpyxl.load_workbook("row col.xlsx")
ws = wb.worksheets[0]
# 按行獲取
for row in ws.rows:
    print([c.value for c in row])
    # # ✌️🐾列表方法
    # c_row = []
    # for c in row:
    #     c_row.append(c.value)
    # print(c_row)

# 按列獲取
for col in ws.columns:
    print([d.value for d in col])

# 最小最大行號, 列號
print(ws.min_row)
print(ws.max_row)
print(ws.min_column)
print(ws.max_column)

# 指定單元行號, 列號
print(ws.cell(4,6).row)
print(ws["F4"].column)

# iter_rows, iter_cols
# for row in ws.iter_rows(min_row=2, min_col= 3): # 可缺省, 則爲實際最大或最小
for row in ws.iter_rows(min_row=1, max_row=4, min_col=1, max_col=5):
    # 🔢
    # for c in row:
    #     print(c.value)

    # 🔢
    print([c.value for c in row][1:2]) # 第二列
    print([c.value for c in row][-1]) # 最後一列
    print([c.value for c in row][0:-1]) # 開始到不包含最後一列

    # 🔢🐾method
    # d= [c.value for c in row]
    # for e in d:
    #     print(e)

# 遍历所有行和单元格
for row in ws.iter_rows(max_row=3, max_col=5):
    for cell in row:
        print(cell.value)

# 解释
# sheet.iter_rows(): 这是 openpyxl 提供的一种方法，用于迭代工作表中的所有行。它返回一个包含所有行的生成器，每一行都是一个包含所有单元格的元组。
# for cell in row:: 这是一个嵌套的循环，用于遍历每一行中的所有单元格。row 是一个包含该行所有单元格的元组，cell 是元组中的每一个单元格对象。