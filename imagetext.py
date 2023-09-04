import torch
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import matplotlib.font_manager

class TextImagePoint:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ('STRING', { 'multiline': True, 'default': '' }),
                "size": ("INT", {"default": 20, "min": 1, "max": 1000}),
                "width": ("INT", {"default": 800, "min": 64, "max": 10000}),
                "height": ("INT", {"default": 1200, "min": 64, "max": 10000}),
                "x_pos": ("INT", {"default": 400, "min": 0, "max": 10000}),
                "y_pos": ("INT", {"default": 400, "min": 0, "max": 10000}),
                "font": ([font.split("\\")[-1] for font in matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf') if font.split(".")[-1] == "ttf"],),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_text"
    OUTPUT_NODE = True
    CATEGORY = "image"

    def generate_text(self, text, size, width, height, x_pos, y_pos, font):
        # generate image with PIL
        image = Image.new('RGB', (width, height))

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", size)
        draw.text((x_pos, y_pos), text, font=font)

        # convert to tensor
        out_image = np.array(image.convert("RGB")).astype(np.float32) / 255.0
        out_image = torch.from_numpy(out_image).unsqueeze(0)

        return (torch.cat([out_image], 0),)

class TextImagePixel:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ('STRING', { 'multiline': True, 'default': '' }),
                "size": ("INT", {"default": 20, "min": 1, "max": 1000}),
                "width": ("INT", {"default": 800, "min": 64, "max": 10000}),
                "height": ("INT", {"default": 1200, "min": 64, "max": 10000}),
                "x_pos": ("INT", {"default": 400, "min": 0, "max": 10000}),
                "y_pos": ("INT", {"default": 400, "min": 0, "max": 10000}),
                "font": ([font.split("\\")[-1] for font in matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf') if font.split(".")[-1] == "ttf"],),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_text"
    OUTPUT_NODE = True
    CATEGORY = "image"

    def generate_text(self, text, size, width, height, x_pos, y_pos, font):
        # generate image with PIL
        image = Image.new('RGB', (width, height))
        
        size = size * 0.75
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", size)
        draw.text((x_pos, y_pos), text, font=font)

        # convert to tensor
        out_image = np.array(image.convert("RGB")).astype(np.float32) / 255.0
        out_image = torch.from_numpy(out_image).unsqueeze(0)

        return (torch.cat([out_image], 0),)
        
NODE_CLASS_MAPPINGS = {
    "Generate Text Image (Point)": TextImagePoint,
    "Generate Text Image (Pixels)": TextImagePixel,
}