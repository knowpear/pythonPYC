import openpyxl
wb = openpyxl.load_workbook("openpyxl cell2.xlsx")

# R1C1 method
total_sum = sum([sh.cell(2, 2).value for sh in wb])
# total_sum = sum(sh.cell(row=2, column=2).value for sh in wb)
print(total_sum)

# A1 method
total_sum2 = sum([sh['B2'].value for sh in wb])
print(total_sum2)

# 🐾笨方法
# s = 0
# for sh in wb.worksheets:
# for sh in wb: # 🐾.worksheets可省略
#     # print(sh.cell(2,2).value)
#     s = s + sh.cell(2,2).value
# print(s)

# 📚GPT4.0分步改寫
# 初始化一个空列表来收集值
# values = []
# # 遍历工作簿中的所有工作表
# for sh in wb:
#     获取当前工作表的第二行第二列的单元格值
#     cell_value = sh.cell(2, 2).value
#     # 将获取到的值添加到列表中
#     values.append(cell_value)
# 计算列表中所有数值的总和
# total_sum = sum(values)
# 打印出总和
# print(total_sum)