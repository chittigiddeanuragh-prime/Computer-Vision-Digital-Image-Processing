"""
Program C: Reading and Displaying Two Images Simultaneously

This program reads two different images from disk and displays
them in separate OpenCV windows side by side.

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
IMAGE1_PATH = os.path.join(SCRIPT_DIR, "Images", "image1.jpg")
IMAGE2_PATH = os.path.join(SCRIPT_DIR, "Images", "image2.jpg")

# --- Read the first image ---
image1 = cv2.imread(IMAGE1_PATH)

# --- Read the second image ---
image2 = cv2.imread(IMAGE2_PATH)

# --- Validate both images ---
if image1 is None:
    print(f"Error: Could not load image from '{IMAGE1_PATH}'")
if image2 is None:
    print(f"Error: Could not load image from '{IMAGE2_PATH}'")

if image1 is not None and image2 is not None:
    print("Both images loaded successfully.")
    print(f"Image 1 dimensions: {image1.shape}")
    print(f"Image 2 dimensions: {image2.shape}")

    # --- Display both images in separate windows ---
    # Each call to cv2.imshow() with a different window name creates a new window
    cv2.imshow("Program C - Image 1", image1)
    cv2.imshow("Program C - Image 2", image2)

    # --- Wait for user input ---
    print("Press any key on either image window to close both...")
    cv2.waitKey(0)

    # --- Close all windows ---
    cv2.destroyAllWindows()
    print("All windows closed successfully.")
else:
    print("Please ensure both image files exist in the Images/ directory.")
