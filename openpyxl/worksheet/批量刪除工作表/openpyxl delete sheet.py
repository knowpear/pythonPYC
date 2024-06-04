import openpyxl
wb = openpyxl.load_workbook("openpyxl cell2.xlsx")
for sh in wb.worksheets:
    if sh.title not in ["1月", "2月", "3月"]:
        wb.remove(sh)
wb.save("openpyxl cell2.xlsx")