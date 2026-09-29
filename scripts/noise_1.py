import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def add_noise_1(
    image: Image.Image,
    stain_count=20,
    speckle_count=300,
    stain_opacity=(8, 35),
    speckle_opacity=(10, 45),
    stain_size=(10, 80),
    grain_strength=3,
):
    """
    Add realistic paper dirt/noise to a scanned-document-like image.

    Includes:
    - Large soft irregular stains
    - Small dirt/speckles
    - Subtle paper discoloration
    - Fine sensor/scanner grain
    """
    image = image.convert("RGB")
    width, height = image.size

    # ---------------------------------------------------------
    # 1. Large irregular stains
    # ---------------------------------------------------------
    stain_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for _ in range(stain_count):
        x = random.randint(0, width)
        y = random.randint(0, height)

        size = random.randint(*stain_size)

        # Irregular polygon instead of perfect ellipse
        points = []

        num_points = random.randint(8, 14)

        for i in range(num_points):
            angle = 2 * np.pi * i / num_points

            radius = size * random.uniform(0.5, 1.2)

            px = x + np.cos(angle) * radius
            py = y + np.sin(angle) * radius * random.uniform(0.5, 1.0)

            points.append((px, py))

        opacity = random.randint(*stain_opacity)

        # Slightly brown/gray dirty paper color
        color = random.choice([
            (80, 70, 55, opacity),
            (100, 90, 70, opacity),
            (70, 70, 65, opacity),
            (120, 105, 80, opacity),
        ])

        draw = ImageDraw.Draw(stain_layer)
        draw.polygon(points, fill=color)

    # Strong blur makes stains look absorbed into paper
    stain_layer = stain_layer.filter(
        ImageFilter.GaussianBlur(
            radius=random.uniform(5, 15)
        )
    )

    image = Image.alpha_composite(
        image.convert("RGBA"),
        stain_layer,
    )

    # ---------------------------------------------------------
    # 2. Small dirt / speckles
    # ---------------------------------------------------------
    speckle_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(speckle_layer)

    for _ in range(speckle_count):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        radius = random.uniform(0.3, 2.0)
        opacity = random.randint(*speckle_opacity)

        color = random.choice([
            (40, 40, 35, opacity),
            (70, 65, 55, opacity),
            (100, 90, 70, opacity),
        ])

        draw.ellipse(
            (
                x - radius,
                y - radius,
                x + radius,
                y + radius,
            ),
            fill=color,
        )

    # Slight blur so speckles don't look digitally generated
    speckle_layer = speckle_layer.filter(
        ImageFilter.GaussianBlur(0.4)
    )

    image = Image.alpha_composite(
        image,
        speckle_layer,
    )

    # ---------------------------------------------------------
    # 3. Subtle paper discoloration
    # ---------------------------------------------------------
    arr = np.asarray(image.convert("RGB")).astype(np.float32)

    low_res_h = max(1, height // 30)
    low_res_w = max(1, width // 30)

    discoloration = np.random.normal(
        loc=0,
        scale=1,
        size=(low_res_h, low_res_w),
    )

    discoloration = Image.fromarray(
        np.uint8(
            np.clip(
                (discoloration + 3) * 35,
                0,
                255,
            )
        )
    )

    discoloration = discoloration.resize(
        (width, height),
        Image.Resampling.BICUBIC,
    )

    discoloration = discoloration.filter(
        ImageFilter.GaussianBlur(20)
    )

    discoloration = (
        np.asarray(discoloration).astype(np.float32) - 105
    )

    arr += discoloration[..., None] * 0.025

    # ---------------------------------------------------------
    # 4. Fine scanner / camera grain
    # ---------------------------------------------------------
    grain = np.random.normal(
        0,
        grain_strength,
        size=(height, width, 1),
    )

    arr += grain

    arr = np.clip(arr, 0, 255).astype(np.uint8)

    return Image.fromarray(arr)