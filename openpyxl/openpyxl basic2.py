import openpyxl
from openpyxl import Workbook, load_workbook

# 新建工作簿
wb = openpyxl.Workbook()
# wb = openpyxl.Workbook() # 完整寫法
ws1 = wb.active # 🐾激活工作表
ws1["A1"].value = "a1"
# 保存工作簿
wb.save("openpyxl basic2.xlsx")

# 讀取工作簿
wb2 = openpyxl.load_workbook("openpyxl basic2.xlsx")
ws2 = wb2.active
ws2["A2"].value = "a2"
wb2.save("openpyxl basic2.xlsx")