import openpyxl
wb = openpyxl.load_workbook("read worksheet.xlsx")
ws = wb.active

a = ws.values
print(a)

l = list(a)
print(l)
for row in l:
    print(row)

t = (l[1][2])
print(t) # result: Ç2, 按列表索引來的