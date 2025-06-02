import os
import numpy as np
from PIL import Image, UnidentifiedImageError


def load_image(path: str) -> np.ndarray:
    """load an image as a numpy array"""
    try:
        image = Image.open(path).convert("RGB")
        return np.asarray(image, dtype=np.uint8)
    except (FileNotFoundError):
        raise FileNotFoundError(f"File not found: {path}")
    except (UnidentifiedImageError):
        raise ValueError(f"The file at {path} is not a valid image") from UnidentifiedImageError


def save_image(image_array: np.ndarray, output_path: str = "output_images") -> None:
    """save a numpy array as an image file"""
    os.makedirs(output_path,exist_ok=True)
    full_path = os.path.join(output_path, "New_image.png")
    to_image = Image.fromarray(image_array)
    to_image.save(full_path)


def check_rgb_uint8(image_array: np.ndarray) -> None:
    if image_array.dtype != np.uint8:
        raise TypeError("image_array must have dtype uint8")
    if image_array.ndim != 3 or image_array.shape[2] != 3:
        raise ValueError("image_array must have shape (H, W, 3)")