import openpyxl
from openpyxl import Workbook, load_workbook
wb = Workbook()
ws = wb.active
ws.title = "Data"
ws.append(["Tim", "is", "great", "!"])
ws.append(["Tim", "is", "great", "!"])
ws.append(["Tim", "is", "great", "!"])
ws.append(["Tim", "is", "great", "!"])
ws.append(["end", ])
wb.save("openpyxl append output.xlsx")