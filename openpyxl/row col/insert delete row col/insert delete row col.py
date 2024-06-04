import openpyxl
wb = openpyxl.load_workbook("insert delete row col.xlsx")
ws = wb.worksheets[0]
ws.insert_cols(1, 1)
ws.insert_rows(1,2)
ws.delete_cols(3, 2)
ws.delete_rows(3,1)

wb.save("insert delete row col output.xlsx")