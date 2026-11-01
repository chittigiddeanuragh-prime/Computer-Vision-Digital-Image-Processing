"""
Program F: Reading and Displaying an Image with Validation

This program reads an image from disk, validates whether the loading
was successful, and displays it using OpenCV.

OpenCV Functions Used:
    - cv2.imread()           : Reads an image from the specified file path
    - cv2.imshow()           : Displays an image in a named window
    - cv2.waitKey(0)         : Waits indefinitely for a key press
    - cv2.destroyAllWindows(): Closes all OpenCV windows
"""

import cv2
import os

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "Images", "image1.jpg")

# --- Read the image ---
print(f"Attempting to load image from: {IMAGE_PATH}")
image = cv2.imread(IMAGE_PATH)

# --- Check whether loading was successful ---
if image is None:
    print("\n[FAILED] Image loading was unsuccessful.")
    print(f"  File path: {IMAGE_PATH}")
    print(f"  File exists: {os.path.exists(IMAGE_PATH)}")
    print("\nTroubleshooting tips:")
    print("  1. Check if the file path is correct")
    print("  2. Ensure the file is a valid image format")
    print("  3. Verify the file is not corrupted")
else:
    print("\n[SUCCESS] Image loaded successfully!")
    print(f"  Dimensions : {image.shape[1]}x{image.shape[0]} pixels")
    print(f"  Channels   : {image.shape[2] if len(image.shape) == 3 else 1}")
    print(f"  Data type  : {image.dtype}")

    # --- Display the image ---
    cv2.imshow("Program F - Image Display", image)

    # --- Wait for user input ---
    print("\nPress any key on the image window to close it...")
    cv2.waitKey(0)

    # --- Close all windows ---
    cv2.destroyAllWindows()
    print("Window closed successfully.")
