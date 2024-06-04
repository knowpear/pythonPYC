import openpyxl
from openpyxl import Workbook, load_workbook

wb = load_workbook("openpyxl basic.xlsx")

ws = wb.active

print(ws)
print(wb.sheetnames)

a = ws["A:C"]
for row in a:
    for cell in row:
        print(cell.value)

print(ws["B2"].value)

ws["B2"].value = "modified b2"
print(ws["A2"].value)

wb.create_sheet("sheet_new")
print(wb.sheetnames)

ws.merge_cells("A1:C1")
ws.merge_cells("A3:C3")
print(ws["B1"].value) # 合併"A1:D1"後, B1爲空

ws.unmerge_cells("A3:C3")

ws.insert_rows(3)
ws.insert_rows(4)
ws.delete_rows(4)

ws.insert_cols(2)
ws.insert_cols(3)
ws.delete_cols(3)

ws.move_range("A2:E5", rows= 2, cols=3)

wb.save("openpyxl basic output.xlsx")
