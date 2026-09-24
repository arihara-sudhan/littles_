import json
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

file_path = "data_/meta.json"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
else:
    print(f"Error: {file_path} not found.")
    data = []

def create_rounded_image(image, radius):
    image = image.convert("RGBA")  # Ensure image has an alpha channel
    mask = Image.new("L", image.size, 0)  # Create a grayscale mask
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, image.size[0], image.size[1]], radius=radius, fill=255)
    rounded_image = Image.new("RGBA", image.size)
    rounded_image.paste(image, (0, 0), mask=mask)
    return rounded_image

def create_card(entry, output_path):
    card_width, card_height = 1000, 1000
    img = Image.new('RGBA', (card_width, card_height), color='white')  # Use RGBA mode
    draw = ImageDraw.Draw(img)

    font_large = ImageFont.truetype("./fonts_/Lato-Bold.ttf", 43)
    font_small = ImageFont.truetype("./fonts_/Lato-Italic.ttf", 39)

    image_filename = entry["name"].lower().replace(" ", "_")
    image_extensions = ['.jpg', '.png', '.webp', '.jpeg', '.avif']
    image_path = next((f"./images/{image_filename}{ext}" for ext in image_extensions if os.path.exists(f"./images/{image_filename}{ext}")), None)

    # Image section
    if image_path:
        try:
            animal_image = Image.open(image_path).resize((800, 800))
            rounded_image = create_rounded_image(animal_image, radius=16)  # 1rem = 16px
            img.paste(rounded_image, ((card_width - 800) // 2, (card_height - 800) // 2 - 50), mask=rounded_image)
        except FileNotFoundError:
            draw.rectangle([(300, 300), (700, 700)], fill="gray")
            draw.text((card_width // 2, card_height // 2), "No Image", fill="white", font=font_small, anchor="mm")
    else:
        draw.rectangle([(300, 300), (700, 700)], fill="gray")
        draw.text((card_width // 2, card_height // 2), "No Image", fill="white", font=font_small, anchor="mm")

    # Common name section
    y_offset = 850 + 20
    bbox = draw.textbbox((0, 0), entry["name"], font=font_large)
    text_width = bbox[2] - bbox[0]
    draw.text(((card_width - text_width) // 2, y_offset), entry["name"], fill="black", font=font_large)

    # Scientific name section
    y_offset += 60
    bbox = draw.textbbox((0, 0), entry["scientific_name"], font=font_small)
    text_width = bbox[2] - bbox[0]
    draw.text(((card_width - text_width) // 2, y_offset), entry["scientific_name"], fill="green", font=font_small)

    # Convert back to RGB for saving (if no transparency is needed)
    img = img.convert("RGB")
    img.save(output_path)


output_dir = "./cards"
os.makedirs(output_dir, exist_ok=True)

for entry in data:
    output_file = f"{output_dir}/card_{entry['number']}.png"
    create_card(entry, output_file)
    print(f"Saved CARD: {entry['name']} : {output_file}")
