from PIL import Image, ImageChops, ImageDraw, ImageFont

def crop_to_content(image, background_color="white", padding=20):
    background = Image.new("RGB", image.size, background_color)

    diff = ImageChops.difference(image, background)
    bbox = diff.getbbox()

    if bbox is None:
        return image

    left, top, right, bottom = bbox

    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(image.width, right + padding)
    bottom = min(image.height, bottom + padding)

    return image.crop((left, top, right, bottom))