import openpyxl
wb = openpyxl.load_workbook("bunch modify sheetnames input.xlsx")
for i in range(1, 5):
        wb.create_sheet(f"Sheet{i+1}")

for n in wb.worksheets:
    # n.title = f"{n.title}" + "公司" # 🐾土方法
    n.title = n.title + "公司"

wb.save("bunch modify sheetnames output.xlsx")