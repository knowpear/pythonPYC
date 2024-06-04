from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook("iterate cells input.xlsx")
ws = wb.active

for row in range(1, 5):
    for col in range(1, 4):
        # char = chr(65 + col) # 底層寫法, 65是A
        char = get_column_letter(col)
        # print(ws[char + str(row)].value) # 遍歷各cell的值
        ws[char + str(row)] = char + str(row)

wb.save("iterate cells output.xlsx")