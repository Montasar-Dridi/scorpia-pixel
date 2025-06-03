from pixel_core import load_image, save_image, invert_colors, blur_image

original_image = load_image("data/faraz_test.jpg")

color_inverted_image = invert_colors(original_image)
blurred_image_gaussian = blur_image(original_image, kernel_size=31, kernel_type="gaussian", padding="constant")
blurred_image_box = blur_image(original_image, kernel_size=31, kernel_type="box", padding="constant")
save_image(color_inverted_image)
save_image(blurred_image_gaussian)
save_image(blurred_image_boxs)