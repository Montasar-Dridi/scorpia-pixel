import numpy as np
from scipy.ndimage import convolve
from filters import blur_image

def test_blur_image_rgb_zero_padding():
    original_array = np.array([
        [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
        [[15, 25, 35], [45, 55, 65], [75, 85, 95]],
        [[20, 30, 40], [50, 60, 70], [80, 90,100]]
    ], dtype=np.uint8)

    kernel = np.ones((3, 3), dtype=np.float32) / 9.0

    expected_array = np.zeros_like(original_array)
    for c in range(3):
        expected_array[:, :, c] = convolve(
            original_array[:, :, c], kernel, mode='constant', cval=0.0
        )

    result = blur_image(original_array, kernel_size=3, padding="constant")

    assert result.shape == expected_array.shape, "Shape mismatch"
    assert np.allclose(result, expected_array, atol=1e-2), "Blur result incorrect" #allclose will allows small tolerance
