"""
Program D: Reading Images in Different Color Modes

This program demonstrates the three main image reading modes in OpenCV:
    1. cv2.IMREAD_COLOR      - Loads image in BGR color (default)
    2. cv2.IMREAD_GRAYSCALE  - Loads image as grayscale
    3. cv2.IMREAD_UNCHANGED  - Loads image as-is (includes alpha channel if present)

OpenCV Functions Used:
    - cv2.imread(path, flag) : Reads an image with the specified color mode
    - cv2.imshow()           : Displays an image in a named window
    - cv2.waitKey(0)         : Waits indefinitely for a key press
    - cv2.destroyAllWindows(): Closes all OpenCV windows
"""

import cv2
import os

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "Images", "image1.jpg")

# --- Read the image in different color modes ---

# Mode 1: cv2.IMREAD_COLOR (flag = 1)
# Loads the image in BGR (Blue, Green, Red) color format
# Any transparency (alpha channel) is ignored
color_image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

# Mode 2: cv2.IMREAD_GRAYSCALE (flag = 0)
# Converts the image to a single-channel grayscale image
gray_image = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

# Mode 3: cv2.IMREAD_UNCHANGED (flag = -1)
# Loads the image as-is, including the alpha channel if present
unchanged_image = cv2.imread(IMAGE_PATH, cv2.IMREAD_UNCHANGED)

# --- Validate images ---
if color_image is None or gray_image is None or unchanged_image is None:
    print(f"Error: Could not load image from '{IMAGE_PATH}'")
    print("Please ensure the image file exists in the Images/ directory.")
else:
    # --- Print dimensions for each mode ---
    print(f"Color image (IMREAD_COLOR) shape:         {color_image.shape}")
    print(f"Grayscale image (IMREAD_GRAYSCALE) shape:  {gray_image.shape}")
    print(f"Unchanged image (IMREAD_UNCHANGED) shape:  {unchanged_image.shape}")

    # --- Display all three versions ---
    cv2.imshow("Color Image (BGR)", color_image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imshow("Unchanged Image", unchanged_image)

    # --- Wait for user input ---
    print("\nPress any key on any image window to close all...")
    cv2.waitKey(0)

    # --- Close all windows ---
    cv2.destroyAllWindows()
    print("All windows closed successfully.")
