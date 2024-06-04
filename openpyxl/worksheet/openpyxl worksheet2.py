import openpyxl
wb = openpyxl.Workbook()
for i in range(1, 4):
    wb.create_sheet()
wb.create_sheet("new", 2) # 第三位置

wb.save("openpyxl worksheet2.xlsx")

# ws = wb.copy_worksheet(wb["new"]) # 未指定名稱則默認sheetname後加` Copy`
# print(ws)
# print(ws.title)

wb.copy_worksheet(wb["new"]).title = "new_DIY"

wb.remove(wb["Sheet1"])

wb.save("openpyxl worksheet2.xlsx")