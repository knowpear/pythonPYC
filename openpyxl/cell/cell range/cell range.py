import openpyxl
from openpyxl.utils import get_column_letter
wb = openpyxl.load_workbook("cell range.xlsx",data_only = True)
ws = wb.worksheets[0]

# 按起始結束單元格
# for row in ws["A1:G3"]:
#     for c in row: # 通過兩次循環, 依次全部打印
#         print(c)
#         print(c.value)
    # print(row)
#
# 按起始結束行號
# for row in ws["1:3"]:
#     print(row) # 使用過的(有數據的單元格都讀取)
#
# # 按起始結束列號
# for col in ws["A:D"]:
#     print(col)
#     # for c in col:
#     #     print(c)

# 按索引讀取
# list(wb.worksheets[0].values)
n1 = list(wb.worksheets[0].values)[1:] # 做切片, 第一行(不包括)以後
print(n1)
# n = list(wb.worksheets[0].values)[1:3] # 做切片, 第一行(不包括)到第三行
# n = list(wb.worksheets[0].values)[0:3][0] # 做切片, 第一行(不包括)到第三行, 只取第一個元祖(即第一行)
n4 = list(wb.worksheets[0].values)[0:3][0:2]
print(n4)

# 迭代器
print([[c.value for c in row] for row in ws["A1:D3"]])

wb.save("cell range.xlsx")