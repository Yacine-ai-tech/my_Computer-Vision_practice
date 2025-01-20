# Contour Detection in Images

This Python script demonstrates how to perform contour detection on an image using OpenCV and visualize the results with Matplotlib. The script processes a sample image, detects contours, and displays both the original image and the processed image with contours drawn.

## Features

- Converts a color image to grayscale.
- Applies Gaussian blur for noise reduction.
- Uses adaptive thresholding to create a binary image.
- Detects contours in the binary image.
- Draws the detected contours on the original image.
- Displays the total number of contours detected on the image.
- Visualizes the original and contour-drawn images side by side.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV
- Matplotlib
- NumPy

## Installation

1. Clone this repository or copy the script file.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. Place your input image (e.g., `shape_for_test.jpeg`) in the desired directory.
2. Update the script to point to the correct path for your image:
   ```python
   img = cv2.imread('/path/to/your/image.jpeg')
   ```
3. Run the script:
   ```bash
   python script_name.py
   ```

## Script Overview

### 1. Load the Image

The script reads the input image and converts it to RGB format for visualization:

```python
img = cv2.imread('/content/shape_for_test.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

### 2. Convert to Grayscale

The RGB image is converted to grayscale for processing:

```python
gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
```

### 3. Apply Gaussian Blur

A Gaussian blur is applied to reduce noise:

```python
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
```

### 4. Adaptive Thresholding

Adaptive thresholding is used to create a binary image:

```python
thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
```

### 5. Detect Contours

Contours are detected from the binary image:

```python
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

### 6. Draw Contours

The detected contours are drawn on a copy of the original image in red:

```python
cv2.drawContours(copy_img, contours, -1, (0, 0, 255), 2)
```

### 7. Annotate Contour Count

The total number of detected contours is displayed on the image:

```python
cv2.putText(copy_img, f"Contours Detected: {len(contours)}", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
```

### 8. Display Results

The original and contour-drawn images are displayed side by side using Matplotlib:

```python
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
    plt.imshow(imgs[i])
plt.tight_layout()
plt.show()
```

## Example Output

When you run the script, you will see two images displayed side by side:

1. **Original Image**
2. **Image with Detected Contours and Annotations**

## Notes

- The script uses adaptive thresholding for improved performance in varying lighting conditions.
- Ensure the image path is correctly set to avoid errors.

## Install Dependencies

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## License

This project is open-source and available under the MIT License.
