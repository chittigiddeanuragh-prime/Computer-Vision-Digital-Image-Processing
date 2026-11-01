# Experiment 01: Reading, Displaying and Saving Images in Different File Formats Using OpenCV

## Experiment Number

**01**

## Experiment Title

Reading, Displaying and Saving Images in Different File Formats Using OpenCV

## Aim

Write a program to read an image from disk, display it, and save it in a different file format.

---

## Software Requirements

| Software   | Version       |
|------------|---------------|
| Python     | 3.8 or above  |
| OpenCV     | 4.x           |
| OS         | Windows / Linux / macOS |

### Installation

```bash
pip install opencv-python
```

---

## Libraries Used

| Library   | Purpose                                |
|-----------|----------------------------------------|
| `cv2`     | OpenCV library for image processing    |
| `os`      | File path handling and directory operations |

---

## OpenCV Functions Used

### 1. `cv2.imread(filename, flag)`

Reads an image from the specified file path.

| Parameter  | Description                                         |
|------------|-----------------------------------------------------|
| `filename` | Path to the image file                              |
| `flag`     | Color mode flag (optional, default: `cv2.IMREAD_COLOR`) |

**Color Mode Flags:**

| Flag                    | Value | Description                                      |
|-------------------------|-------|--------------------------------------------------|
| `cv2.IMREAD_COLOR`      | 1     | Loads image in BGR color (default)               |
| `cv2.IMREAD_GRAYSCALE`  | 0     | Loads image as grayscale                         |
| `cv2.IMREAD_UNCHANGED`  | -1    | Loads image as-is (includes alpha channel)       |

**Returns:** A NumPy array representing the image, or `None` if loading fails.

### 2. `cv2.imshow(window_name, image)`

Displays an image in a named window.

| Parameter     | Description                     |
|---------------|---------------------------------|
| `window_name` | Title of the display window     |
| `image`       | Image array to display          |

### 3. `cv2.waitKey(delay)`

Waits for a key event for the specified duration.

| Parameter | Description                                           |
|-----------|-------------------------------------------------------|
| `delay`   | Time in milliseconds. `0` means wait indefinitely.    |

**Returns:** ASCII code of the key pressed, or `-1` if no key was pressed within the timeout.

### 4. `cv2.destroyAllWindows()`

Closes all OpenCV display windows. Takes no parameters.

### 5. `cv2.imwrite(filename, image)`

Saves an image to the specified file path.

| Parameter  | Description                     |
|------------|---------------------------------|
| `filename` | Output file path (format is determined by the file extension) |
| `image`    | Image array to save             |

**Returns:** `True` if the image was saved successfully, `False` otherwise.

---

## Programs

### Program A: `program_A_read_image.py`

**Description:** Reads an image from disk using `cv2.imread()`, displays it using `cv2.imshow()`, waits for a key press using `cv2.waitKey(0)`, and closes the window using `cv2.destroyAllWindows()`.

**Key Concepts:** Basic image I/O operations in OpenCV.

---

### Program B: `program_B_waitkey_demo.py`

**Description:** Displays an image for 3000 milliseconds (3 seconds) to demonstrate the timed functionality of `cv2.waitKey(3000)`. The window closes automatically after the timeout or when a key is pressed.

**Key Concepts:** Timed display, understanding `waitKey()` return values.

---

### Program C: `program_C_read_two_images.py`

**Description:** Reads two different images from disk and displays both in separate OpenCV windows simultaneously. Waits for user input and then closes all windows.

**Key Concepts:** Multiple window management, loading multiple images.

---

### Program D: `program_D_different_color_modes.py`

**Description:** Reads the same image using three different color modes — `IMREAD_COLOR`, `IMREAD_GRAYSCALE`, and `IMREAD_UNCHANGED` — and displays all three versions to compare the differences.

**Key Concepts:** Image color spaces, channel information, `imread` flags.

---

### Program E: `program_E_image_dimensions.py`

**Description:** Reads an image, verifies whether it loaded successfully, and prints its dimensions (height, width, channels) using `image.shape`.

**Key Concepts:** Image metadata, NumPy array properties, error handling.

---

### Program F: `program_F_read_and_display_image.py`

**Description:** Reads an image with comprehensive validation, including checking file existence, and displays it using OpenCV. Provides detailed troubleshooting tips if loading fails.

**Key Concepts:** Robust image loading, input validation, debugging techniques.

---

### Program G: `program_G_save_different_formats.py`

**Description:** Reads an image and saves it in five different file formats: JPEG, PNG, BMP, TIFF, and WEBP. Each format is saved in its own subdirectory under `Outputs/`.

**Key Concepts:** Image format conversion, `cv2.imwrite()`, directory management.

---

## Expected Outputs

### Program A
- A window displaying the loaded image.
- Console output confirming successful loading.

### Program B
- A window displaying the image for 3 seconds.
- Console output indicating whether a key was pressed or the timer expired.

### Program C
- Two separate windows displaying two different images.

### Program D
- Three windows showing the same image in color, grayscale, and unchanged modes.
- Console output showing the shape (dimensions) of each version.

### Program E
- Console output displaying image dimensions:
  ```
  Image Shape   : (height, width, 3)
  Height        : xxx pixels
  Width         : xxx pixels
  Channels      : 3 (BGR color image)
  ```

### Program F
- A window displaying the image after successful validation.
- Detailed console output about image properties.

### Program G
- The original image displayed in a window.
- Five copies of the image saved in different formats under `Outputs/`.
- Console output confirming each save operation.

---

## How to Run

1. **Install OpenCV:**
   ```bash
   pip install opencv-python
   ```

2. **Navigate to the experiment directory:**
   ```bash
   cd 01-Image-Reading-Displaying-and-Saving
   ```

3. **Place your images** in the `Images/` directory (sample images are provided).

4. **Run any program:**
   ```bash
   python program_A_read_image.py
   python program_B_waitkey_demo.py
   python program_C_read_two_images.py
   python program_D_different_color_modes.py
   python program_E_image_dimensions.py
   python program_F_read_and_display_image.py
   python program_G_save_different_formats.py
   ```

---

## Directory Structure

```
01-Image-Reading-Displaying-and-Saving/
│
├── README.md
├── program_A_read_image.py
├── program_B_waitkey_demo.py
├── program_C_read_two_images.py
├── program_D_different_color_modes.py
├── program_E_image_dimensions.py
├── program_F_read_and_display_image.py
├── program_G_save_different_formats.py
│
├── Images/
│   ├── image1.jpg
│   └── image2.jpg
│
└── Outputs/
    ├── JPEG/
    ├── PNG/
    ├── BMP/
    ├── TIFF/
    └── WEBP/
```

---

## Learning Outcomes

After completing this experiment, students will be able to:

1. **Read images** from disk using `cv2.imread()` with different color mode flags.
2. **Display images** in windows using `cv2.imshow()` and manage window lifecycle.
3. **Handle user input** using `cv2.waitKey()` with both timed and indefinite waits.
4. **Manage OpenCV windows** using `cv2.destroyAllWindows()`.
5. **Save images** in multiple file formats (JPEG, PNG, BMP, TIFF, WEBP) using `cv2.imwrite()`.
6. **Validate image loading** by checking for `None` return values.
7. **Inspect image properties** such as dimensions, channels, and data types using NumPy array attributes.
8. **Use relative paths** for portable and cross-platform image file handling.
9. **Create directory structures** programmatically using `os.makedirs()`.

---

## Author

**C. Anuragh**

---
