import openpyxl
wb = openpyxl.Workbook()
ws = wb.worksheets[0]
ws.append([1,2,3,4,5])
ws.append((1,2,3,4,5))
ws.append(range(1,6))
ws.append({1:"張三", 4:"18"}) # 字典: 1, 2代表列數
ws.append({"A":"張三", "D":"18"}) # 字典: A, B代表列數
wb.save("cell batch write.xlsx")