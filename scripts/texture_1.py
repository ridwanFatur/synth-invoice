import numpy as np
from PIL import Image, ImageFilter


def create_texture_1(width, height, num_wrinkles=15):
    texture = np.zeros((height, width), dtype=np.float32)

    yy, xx = np.meshgrid(
        np.arange(height),
        np.arange(width),
        indexing="ij",
    )

    for _ in range(num_wrinkles):
        x0 = np.random.randint(0, width)
        y0 = np.random.randint(0, height)

        angle = np.random.uniform(0, np.pi)

        distance = (
            (xx - x0) * np.cos(angle)
            + (yy - y0) * np.sin(angle)
        )

        wrinkle_width = np.random.uniform(5, 20)

        wrinkle = np.exp(
            -(distance ** 2)
            / (2 * wrinkle_width ** 2)
        )

        texture += wrinkle

    texture -= texture.min()
    texture /= texture.max() + 1e-8

    # Smooth
    texture_image = Image.fromarray(
        (texture * 255).astype(np.uint8)
    )

    texture_image = texture_image.filter(
        ImageFilter.GaussianBlur(3)
    )

    return np.array(texture_image).astype(np.float32) / 255.0


def apply_paper_texture_1(
    image,
    texture,
    displacement=8,
    shading_strength=0.25,
):
    image = image.convert("RGB")

    image_array = np.array(image).astype(np.float32)

    height, width = image_array.shape[:2]

    # Resize texture jika ukurannya berbeda
    texture_image = Image.fromarray(
        (texture * 255).astype(np.uint8)
    ).resize((width, height))

    texture = np.array(texture_image).astype(np.float32) / 255.0

    # ---------------------------------------------------------
    # 1. Calculate texture gradient
    # ---------------------------------------------------------

    gradient_y, gradient_x = np.gradient(texture)

    # Normalize gradient
    gradient_x /= np.max(np.abs(gradient_x)) + 1e-8
    gradient_y /= np.max(np.abs(gradient_y)) + 1e-8

    # ---------------------------------------------------------
    # 2. Displacement
    # ---------------------------------------------------------

    map_x, map_y = np.meshgrid(
        np.arange(width),
        np.arange(height),
    )

    map_x = map_x + gradient_x * displacement
    map_y = map_y + gradient_y * displacement

    # Clamp
    map_x = np.clip(map_x, 0, width - 1)
    map_y = np.clip(map_y, 0, height - 1)

    # ---------------------------------------------------------
    # 3. Bilinear sampling
    # ---------------------------------------------------------

    x0 = np.floor(map_x).astype(np.int32)
    x1 = np.clip(x0 + 1, 0, width - 1)

    y0 = np.floor(map_y).astype(np.int32)
    y1 = np.clip(y0 + 1, 0, height - 1)

    wx = map_x - x0
    wy = map_y - y0

    top = (
        image_array[y0, x0] * (1 - wx[..., None])
        + image_array[y0, x1] * wx[..., None]
    )

    bottom = (
        image_array[y1, x0] * (1 - wx[..., None])
        + image_array[y1, x1] * wx[..., None]
    )

    result = (
        top * (1 - wy[..., None])
        + bottom * wy[..., None]
    )

    # ---------------------------------------------------------
    # 4. Add lighting/shading from texture
    # ---------------------------------------------------------

    shade = (
        gradient_x * 0.7
        + gradient_y * 0.7
    )

    shade = shade[..., None]

    result = result + shade * (255 * shading_strength)

    result = np.clip(result, 0, 255)

    return Image.fromarray(result.astype(np.uint8))