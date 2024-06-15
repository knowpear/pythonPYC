from PIL import Image
from pathlib import Path
import logging

# 定义图片输入文件夹路径
images_folder = Path('./- Samples/imgFolder/')
# 定义图片输出文件夹路径
output_folder = Path('./- Samples/output_imgFolder/')

def iterate_folder_files1(input_path_root, output_path_root):
    """
    遍历指定文件夹中的所有文件，并对每个文件调用resize_image函数。
    input_path_root: Path对象，表示输入文件夹路径。
    output_path_root: Path对象，表示输出文件夹路径。
    """
    # 遍历输入文件夹中的所有项
    for file in input_path_root.glob('*'):
        # 检查项是否为文件
        if file.is_file():
            # ⭐構建輸入和輸出路徑範例
            # 以输入文件为基准，确定输出文件的路径和名称
            input_file = file
            # 拼接构建输出文件的完整路径和文件名
            output_file = output_path_root / file.name
            # 调用图像缩放函数，处理输入文件并保存到指定的输出文件
            resize_image(2, input_file, output_file)

# resize, 既轉換, 又保存
def resize_image(scale, input_file, output_file):
    """
    参数:
    input_file: Path对象，表示输入的图片文件路径。
    output_file: Path对象，表示输出的图片文件路径。
    """
    # 比例
    scale_factor = scale
    try:
        with Image.open(input_file) as image:
            # 原尺寸
            width = image.width
            height = image.height

            # 缩放图片到指定大小
            resized_img = image.resize((round(width*scale_factor), round(height*scale_factor)), resample= Image.LANCZOS)
            # 保存缩放后的图片
            resized_img.save(output_file, optimize=True, quality=85)
            # 打印图片缩放完成的消息
            logging.info(f'{input_file} resized')
    except Exception as e:
        logging.error(f"处理图片 {input_file.name} 时出现错误: {e}")

# 调用函数遍历并缩放图片文件夹中的所有图片
iterate_folder_files1(images_folder, output_folder)
