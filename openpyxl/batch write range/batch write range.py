import openpyxl
wb = openpyxl.load_workbook("batch write range.xlsx")
ws = wb.worksheets[0]
for row in ws["A1:D3"]:
    for c in row:
        c.value = 100
wb.save("batch write range.xlsx")