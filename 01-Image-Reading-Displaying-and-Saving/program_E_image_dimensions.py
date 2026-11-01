"""
Program E: Verifying Image Loading and Printing Dimensions

This program reads an image, verifies whether it loaded successfully,
and prints its dimensions (height, width, and number of channels).

OpenCV Functions Used:
    - cv2.imread()   : Reads an image from the specified file path
    - image.shape    : Returns a tuple (height, width, channels) for color images
                       or (height, width) for grayscale images
"""

import cv2
import os

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "Images", "image1.jpg")

# --- Read the image ---
image = cv2.imread(IMAGE_PATH)

# --- Verify whether the image loaded successfully ---
if image is None:
    print(f"Error: Failed to load image from '{IMAGE_PATH}'")
    print("Possible reasons:")
    print("  - The file does not exist at the specified path")
    print("  - The file format is not supported")
    print("  - The file is corrupted")
else:
    print(f"Image loaded successfully from: {IMAGE_PATH}")
    print()

    # --- Print image dimensions ---
    # image.shape returns:
    #   - (height, width, channels) for color images
    #   - (height, width) for grayscale images
    dimensions = image.shape
    print(f"Image Shape   : {dimensions}")
    print(f"Height        : {dimensions[0]} pixels")
    print(f"Width         : {dimensions[1]} pixels")

    if len(dimensions) == 3:
        print(f"Channels      : {dimensions[2]} (BGR color image)")
    else:
        print(f"Channels      : 1 (Grayscale image)")

    # --- Print additional image information ---
    print(f"Data Type     : {image.dtype}")
    print(f"Total Pixels  : {image.size}")
