import openpyxl

wb = openpyxl.load_workbook("openpyxl worksheet.xlsx")
ws1 = wb.active # 激活當前工作表
ws2 = wb.worksheets[1] # 以索引形式獲取工作表
ws3 = wb["Sheet4"] # 以名稱形式獲取工作表
print(ws1)
print(ws2)
print(ws3)

# 遍歷工作表
for sh in wb.worksheets:
    print(sh)

# 遍歷工作表名
for shn in wb.sheetnames:
    print(shn)

# 獲取工作表名
print(wb.worksheets[1].title)

# 修改工作表名
wb.worksheets[1].title = "modified Sheet2"

wb.save(("openpyxl basic3.xlsx"))