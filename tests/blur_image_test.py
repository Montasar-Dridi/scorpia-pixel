import numpy as np
from scipy.ndimage import convolve
from filters import blur_image

def test_blur_image_box_and_gaussian():
    original_array = np.array([
        [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
        [[15, 25, 35], [45, 55, 65], [75, 85, 95]],
        [[20, 30, 40], [50, 60, 70], [80, 90,100]]
    ], dtype=np.uint8)

    # Common settings
    kernel_size = 3
    pad_mode = 'constant'

    # --- BOX FILTER TEST ---
    box_kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
    expected_box = np.stack([
        convolve(original_array[:, :, c], box_kernel, mode=pad_mode, cval=0.0)
        for c in range(3)
    ], axis=-1).astype(np.uint8)

    result_box = blur_image(original_array, kernel_size=kernel_size, kernel_type="box", padding=pad_mode)

    assert result_box.shape == expected_box.shape, "Box filter: Shape mismatch"
    assert np.allclose(result_box, expected_box, atol=1), "Box filter: Result mismatch"

    # --- GAUSSIAN FILTER TEST ---
    # Just run your blur_image implementation
    result_gaussian = blur_image(original_array, kernel_size=kernel_size, kernel_type="gaussian", padding=pad_mode)

    # No strict expected array here; we just check the shape and dtype
    assert result_gaussian.shape == original_array.shape, "Gaussian filter: Shape mismatch"
    assert result_gaussian.dtype == np.uint8, "Gaussian filter: Dtype should be uint8"
    assert not np.array_equal(result_box, result_gaussian), "Box and Gaussian results should differ"
