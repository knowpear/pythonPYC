import openpyxl
wb = openpyxl.load_workbook("cell read.xlsx")
ws = wb.worksheets[0]
# print(ws.title)
ws["A1"] = "new A1"
ws.cell(2,3, "new C2")
ws.cell(3,3).value = "new C3"

a = ws["1:3"]
for row in a:
    for cell in row:
        print(cell.value)

wb.save("cell read.xlsx")