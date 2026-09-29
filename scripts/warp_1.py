import random

import cv2
import numpy as np
from PIL import Image


def warp_paper_1(
    image: Image.Image,
    padding=50,
    rotation_range=(-3.0, 3.0),
    bend_strength=0.04,
    perspective_strength=0.02,
    horizontal_bend=0.015,
):
    """
    Simulate a physically deformed paper without cropping.

    Args:
        image: Input PIL image.
        padding: Extra white padding around the paper.
        rotation_range: Random global rotation range in degrees.
        bend_strength: Strength of vertical bending.
        perspective_strength: Strength of local rotation/deformation.
        horizontal_bend: Strength of horizontal bending.
    """
    image = image.convert("RGB")

    # ---------------------------------------------------------
    # 1. Add padding
    # ---------------------------------------------------------
    width, height = image.size

    padded = Image.new(
        "RGB",
        (
            width + padding * 2,
            height + padding * 2,
        ),
        (255, 255, 255),
    )

    padded.paste(
        image,
        (padding, padding),
    )

    image = padded

    width, height = image.size

    image_np = np.asarray(image)

    # ---------------------------------------------------------
    # 2. Random global rotation
    # ---------------------------------------------------------
    angle = random.uniform(*rotation_range)

    center = (
        width / 2,
        height / 2,
    )

    rotation_matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0,
    )

    image_np = cv2.warpAffine(
        image_np,
        rotation_matrix,
        (width, height),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(255, 255, 255),
    )

    # ---------------------------------------------------------
    # 3. Coordinate grid
    # ---------------------------------------------------------
    yy, xx = np.meshgrid(
        np.arange(height, dtype=np.float32),
        np.arange(width, dtype=np.float32),
        indexing="ij",
    )

    x = xx / width
    y = yy / height

    # ---------------------------------------------------------
    # 4. Vertical bending
    # ---------------------------------------------------------
    vertical_bend = (
        np.sin(y * np.pi)
        * np.sin((x - 0.5) * np.pi)
    )

    dx = (
        vertical_bend
        * width
        * bend_strength
    )

    # ---------------------------------------------------------
    # 5. Horizontal bending
    # ---------------------------------------------------------
    horizontal_curve = (
        np.sin(x * np.pi)
        * np.sin(y * np.pi)
    )

    dy = (
        horizontal_curve
        * height
        * horizontal_bend
    )

    # ---------------------------------------------------------
    # 6. Different orientation from top -> bottom
    # ---------------------------------------------------------
    local_rotation = (
        (y - 0.5)
        * perspective_strength
        * width
    )

    dx += local_rotation * (x - 0.5)

    # ---------------------------------------------------------
    # 7. Smooth random deformation
    # ---------------------------------------------------------
    noise_small = np.random.normal(
        0,
        1,
        size=(
            max(2, height // 40),
            max(2, width // 40),
        ),
    ).astype(np.float32)

    noise_small = cv2.resize(
        noise_small,
        (width, height),
        interpolation=cv2.INTER_CUBIC,
    )

    noise_small = cv2.GaussianBlur(
        noise_small,
        (0, 0),
        sigmaX=20,
    )

    noise_small /= (
        np.max(np.abs(noise_small)) + 1e-6
    )

    dx += noise_small * width * 0.008
    dy += noise_small * height * 0.008

    # ---------------------------------------------------------
    # 8. Remapping
    # ---------------------------------------------------------
    map_x = xx + dx
    map_y = yy + dy

    warped = cv2.remap(
        image_np,
        map_x,
        map_y,
        interpolation=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(255, 255, 255),
    )

    return Image.fromarray(warped)