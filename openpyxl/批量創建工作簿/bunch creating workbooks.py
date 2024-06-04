import openpyxl
from openpyxl import Workbook
for i in range(1, 4):
    wb = openpyxl.Workbook()
    wb.save(f'{i}月.xlsx')