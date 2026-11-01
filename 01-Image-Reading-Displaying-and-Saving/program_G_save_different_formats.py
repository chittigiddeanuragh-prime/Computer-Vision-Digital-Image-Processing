"""
Program G: Saving an Image in Multiple File Formats

This program reads an image and saves it in five different file formats:
    - JPEG (.jpg)
    - PNG  (.png)
    - BMP  (.bmp)
    - TIFF (.tiff)
    - WEBP (.webp)

OpenCV Functions Used:
    - cv2.imread()           : Reads an image from the specified file path
    - cv2.imshow()           : Displays an image in a named window
    - cv2.imwrite()          : Saves an image to the specified file path
    - cv2.waitKey(0)         : Waits indefinitely for a key press
    - cv2.destroyAllWindows(): Closes all OpenCV windows
"""

import cv2
import os

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "Images", "image1.jpg")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "Outputs")

# --- Define output formats and their subdirectories ---
formats = {
    "JPEG": "output_image.jpg",
    "PNG":  "output_image.png",
    "BMP":  "output_image.bmp",
    "TIFF": "output_image.tiff",
    "WEBP": "output_image.webp",
}

# --- Read the image ---
image = cv2.imread(IMAGE_PATH)

if image is None:
    print(f"Error: Could not load image from '{IMAGE_PATH}'")
    print("Please ensure the image file exists in the Images/ directory.")
else:
    print(f"Image loaded successfully from: {IMAGE_PATH}")
    print(f"Image dimensions: {image.shape}")
    print()

    # --- Display the original image ---
    cv2.imshow("Program G - Original Image", image)

    # --- Save the image in each format ---
    print("Saving image in different formats:")
    print("-" * 50)

    for fmt, filename in formats.items():
        # Create the output subdirectory if it does not exist
        fmt_dir = os.path.join(OUTPUT_DIR, fmt)
        os.makedirs(fmt_dir, exist_ok=True)

        # Build the full output path
        output_path = os.path.join(fmt_dir, filename)

        # cv2.imwrite() saves the image to the specified path
        # The file format is determined by the file extension
        success = cv2.imwrite(output_path, image)

        if success:
            print(f"  [SUCCESS] {fmt:5s} -> {output_path}")
        else:
            print(f"  [FAILED]  {fmt:5s} -> Could not save to {output_path}")

    print("-" * 50)
    print("\nAll formats saved successfully!")

    # --- Wait for user input ---
    print("\nPress any key on the image window to close it...")
    cv2.waitKey(0)

    # --- Close all windows ---
    cv2.destroyAllWindows()
    print("Window closed.")
