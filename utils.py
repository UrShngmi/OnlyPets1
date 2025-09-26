import logging
from PIL import Image, ImageTk, ImageDraw, ImageFont
import customtkinter as ctk

def setup_logging():
    """
    Sets up basic logging for the application.
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logging()

def load_image(path, size, placeholder=True):
    """
    Loads an image from a path, resizes it, and returns a CTkImage object.
    If the image is not found, it can generate a placeholder.
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        if placeholder:
            # Generate a placeholder image
            img = Image.new('RGB', size, color = (100, 100, 100))
            d = ImageDraw.Draw(img)
            try:
                # Use a simple font if available
                font = ImageFont.truetype("arial.ttf", 20)
            except IOError:
                font = ImageFont.load_default()
            
            text = f"{size[0]}x{size[1]}"
            textwidth, textheight = d.textbbox((0,0),text, font=font)[2:]
            
            x = (size[0] - textwidth) / 2
            y = (size[1] - textheight) / 2
            d.text((x, y), text, fill=(255, 255, 255), font=font)
        else:
            return None
            
    img = img.resize(size, Image.LANCZOS)
    return ctk.CTkImage(light_image=img, dark_image=img, size=size)
