import openpyxl
wb = openpyxl.Workbook()
for i in range(1, 13):
    ws = wb.create_sheet(f"{i}月")
# wb.remove(wb["Sheet"])
# wb.remove(wb.worksheets[0])
wb.remove(wb.active)
wb.save("bunch creat worksheet output.xlsx")