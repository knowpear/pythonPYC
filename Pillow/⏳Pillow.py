from PIL import Image

def shrink_image(input_path, output_path, max_width, max_height):
    with Image.open(input_path) as img:
        # Calculate scaling factor
        width, height = img.size
        scale = min(max_width / width, max_height / height)

        # Resize the image
        new_size = (int(width * scale), int(height * scale))
        img_resized = img.resize(new_size, resample=Image.LANCZOS)

        # Save the resized image
        img_resized.save(output_path, format="JPEG", quality=90)

# Usage
shrink_image("original.jpg", "shrunk.jpg", 800, 600)
