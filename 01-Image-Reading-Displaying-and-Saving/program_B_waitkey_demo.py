"""
Program B: Demonstrating cv2.waitKey() with a Timed Display

This program displays an image for a specified duration (3000 milliseconds)
and demonstrates how cv2.waitKey() works with a timeout value.

OpenCV Functions Used:
    - cv2.imread()           : Reads an image from the specified file path
    - cv2.imshow()           : Displays an image in a named window
    - cv2.waitKey(ms)        : Waits for the specified milliseconds or a key press
    - cv2.destroyAllWindows(): Closes all OpenCV windows
"""

import cv2
import os

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "Images", "image1.jpg")
DISPLAY_TIME_MS = 3000  # Display duration in milliseconds (3 seconds)

# --- Read the image ---
image = cv2.imread(IMAGE_PATH)

if image is None:
    print(f"Error: Could not load image from '{IMAGE_PATH}'")
    print("Please ensure the image file exists in the Images/ directory.")
else:
    print(f"Image loaded successfully.")
    print(f"Displaying image for {DISPLAY_TIME_MS / 1000:.0f} seconds...")

    # --- Display the image ---
    cv2.imshow("Program B - Timed Display (3 seconds)", image)

    # --- Wait for 3000 milliseconds (3 seconds) ---
    # cv2.waitKey(3000) waits for 3 seconds OR until the user presses a key
    # It returns the ASCII code of the key pressed, or -1 if no key was pressed
    key = cv2.waitKey(DISPLAY_TIME_MS)

    if key == -1:
        print("Time elapsed. No key was pressed.")
    else:
        print(f"Key pressed: '{chr(key & 0xFF)}' (ASCII code: {key & 0xFF})")

    # --- Close all windows ---
    cv2.destroyAllWindows()
    print("Window closed.")
