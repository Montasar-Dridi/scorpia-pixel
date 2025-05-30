import numpy as np
from filters import invert_colors


def test_invert_color():
    original_array = np.array(
        [
            [[0,   0,   0],   [34, 100, 200],   [255, 255, 255]],
            [[128,  64,  32],   [50, 180,   0],   [200,  40, 120]],
            [[255,   0, 128],   [15,  90, 255],   [75,  75,  75]],
        ],
        dtype=np.uint8
    )

    expected_array = np.array(
        [
            [[255, 255, 255],   [221, 155,  55],   [0,   0,   0]],
            [[127, 191, 223],   [205,  75, 255],   [55, 215, 135]],
            [[  0, 255, 127],   [240, 165,   0],   [180, 180, 180]],
        ],
        dtype=np.uint8
    )

    result = invert_colors(original_array, in_place=True)
    assert np.array_equal(result, expected_array)
