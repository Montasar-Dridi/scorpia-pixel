
# Scorpia-Pixel

Hey there! Scorpia-Pixel is my personal sandbox for learning image-processing in Python.
If you just want to flip colors or blur a photo for fun, you’re in the right place.
If you need millisecond-level performance for production… probably look elsewhere (for now 😉).


## Why I built it

I learn best by doing, so I started hacking together tiny filters—first an RGB invert, then a box blur, and the rabbit hole just kept going.
Publishing the code on PyPI felt like the perfect excuse to practise packaging, testing, and documentation.
You’re welcome to poke around, break things, and tell me what I did wrong—friendly bug reports are gold.

## What it can do today

* Invert colors: turn a picture into its photo-negative twin.
* Blur images: box blur, Gaussian blur – soften edges with your choice of kernel.
* Simple I/O helpers: load_image() and save_image() so you don’t have to remember Pillow’s API.
Planned (in no particular order):

Sobel / edge detection
Fancy CLI with progress bars
GPU acceleration (one day…)


## Installation

#### The easy way
pip install scorpia-pixel

#### Or, if you enjoy living on the bleeding edge:
git clone https://github.com/Montasar-Dridi/scorpia-pixel.git \
cd scorpia-pixel \
pip install .

    
## Demo
```
from pixel_core import load_image, save_image, blur_image, invert_colors

# 1. Load an image
img = load_image("input.png")

# 2. Apply filters
blurred = blur_image(img, kernel_size=5)
negative = invert_colors(img)

# 3. Save the results
save_image(blurred, "output/blurred.png")
save_image(negative, "output/negative.png")
```
## Project Layout
```
scorpia-pixel/
│
├── pixel_core/          # import this as `pixel_core`
│   ├── __init__.py      # re-exports blur_image, invert_colors, etc.
│   ├── filters.py       # the fun stuff
│   └── image_utils.py   # load / save helpers
│
├── tests/
│   ├── blur_image_test.py
│   └── invert_filter_test.py
│
├── requirements.txt
└── README.md
```
## Who am I
I’m Montasar Dridi, a data scientist who enjoys tinkering with computer vision, AI, and anything that looks cool in a terminal window.
Check out the rest of the Scorpia experiments on my GitHub: https://github.com/Montasar-Dridi

