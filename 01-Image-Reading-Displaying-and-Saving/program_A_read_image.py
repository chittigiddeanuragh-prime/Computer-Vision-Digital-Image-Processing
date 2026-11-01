"""
Program A: Reading and Displaying an Image Using OpenCV

This program demonstrates the basic operations of reading an image
from disk, displaying it in a window, and properly closing the window.

OpenCV Functions Used:
    - cv2.imread()           : Reads an image from the specified file path
    - cv2.imshow()           : Displays an image in a named window
    - cv2.waitKey(0)         : Waits indefinitely for a key press
    - cv2.destroyAllWindows(): Closes all OpenCV windows
"""

import cv2
import os

# --- Configuration ---
# Using relative path from the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "Images", "image1.jpg")

# --- Read the image from disk ---
# cv2.imread() loads an image from the specified file
# By default, it reads the image in BGR (Blue, Green, Red) color format
image = cv2.imread(IMAGE_PATH)

# --- Validate that the image was loaded successfully ---
if image is None:
    print(f"Error: Could not load image from '{IMAGE_PATH}'")
    print("Please ensure the image file exists in the Images/ directory.")
else:
    print(f"Image loaded successfully from: {IMAGE_PATH}")
    print(f"Image dimensions: {image.shape}")

    # --- Display the image in a window ---
    # cv2.imshow() creates a window with the given name and displays the image
    cv2.imshow("Program A - Display Image", image)

    # --- Wait for a key press ---
    # cv2.waitKey(0) waits indefinitely until the user presses any key
    # The argument 0 means "wait forever"
    print("Press any key on the image window to close it...")
    cv2.waitKey(0)

    # --- Close all OpenCV windows ---
    # cv2.destroyAllWindows() closes all the windows created by OpenCV
    cv2.destroyAllWindows()
    print("All windows closed successfully.")
