import openpyxl
wb = openpyxl.load_workbook("openpyxl cell.xlsx")
# ws = wb.active # 🐾後續方法無提示
ws = wb.worksheets[0] # 🐾後續方法有提示
# A1表示法
print(ws["A1"].value)
# R1C1表示法
print(ws.cell(1,1).value)

# 一次性方法
print(openpyxl.load_workbook("openpyxl cell.xlsx").worksheets[0]["B1"].value)
print(openpyxl.load_workbook("openpyxl cell.xlsx").worksheets[0].cell(1,2).value)