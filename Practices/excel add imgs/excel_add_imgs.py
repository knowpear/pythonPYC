import openpyxl
from openpyxl.drawing.image import Image
from PIL import Image as PILImage
import os

def insert_images_to_excel(excel_path, images_folder):
    # 打开 Excel 文件
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb.active

    # 遍历所有单元格
    for row in sheet.iter_rows():
        for cell in row:
            # 检查单元格是否有图片名称
            if cell.value and isinstance(cell.value, str):
                image_name = cell.value.strip()  # 获取单元格内的图片名称
                image_path = os.path.join(images_folder, image_name)

                # 检查图片文件是否存在
                if os.path.exists(image_path):
                    # 加载图片并调整大小
                    img = PILImage.open(image_path)
                    img.thumbnail((100, 100), PILImage.LANCZOS)  # 调整图片大小，保持比例
                    img.save(image_path)  # 保存调整后的图片

                    # 插入图片到单元格
                    img = Image(image_path)
                    img.anchor = cell.coordinate  # 设定图片插入的位置
                    sheet.add_image(img)
                else:
                    print(f"图片 '{image_name}' 不存在于目录 '{images_folder}' 中")

    # 保存修改后的 Excel 文件
    wb.save(output_path)


# 设置 Excel 文件路径和图片文件夹路径
excel_path = "myExcel.xlsx"
images_folder = "imgFolder"
output_path = r"myExcel_Output.xlsx"

insert_images_to_excel(excel_path, images_folder)
