# 🧙🏻使用opencv 調整圖片尺寸, 不損失品質. 輸入folder 爲images_folder = r"C:\Users\DaiYi\Desktop\营业厅资产统计(202406051240)\assembly"; 輸出folder爲output_folder = r"C:\Users\DaiYi\Desktop\assembly"
from PIL import Image
import os
from pathlib import Path

# 输入和输出文件夹
images_folder = Path(r"C:\Users\DaiYi\Desktop\营业厅资产统计(202406051240)\assembly")
output_folder = Path(r"C:\Users\DaiYi\Desktop\assembly")

# 确保输出文件夹存在
output_folder.mkdir(parents=True, exist_ok=True)

# 目标尺寸
width, height = 600, 600  # 举例，您可以根据需要设置

# 遍历输入文件夹中的所有图片文件
for image_path in images_folder.glob('*.*'):
    try:
        # 读取图片
        with Image.open(image_path) as img:
            # 调整图片尺寸
            resized_img = img.resize((width, height), Image.LANCZOS)
            # 构建输出路径
            output_image_path = output_folder / image_path.name
            # 保存调整尺寸后的图片
            resized_img.save(output_image_path, optimize=True, quality=85) # optimize=True, quality=85是從網上抄得的, 不知道有沒有用
            print(f"图片 {image_path.name} 处理成功")
    except Exception as e:
        print(f"处理图片 {image_path.name} 时出现错误: {e}")

