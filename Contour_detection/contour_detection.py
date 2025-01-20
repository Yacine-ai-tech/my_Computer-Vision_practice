# Import necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
img = cv2.imread('./shape_for_test.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur for noise reduction
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding for better edge detection in varying lighting
thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

# Detect contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the image
copy_img = img.copy()
cv2.drawContours(copy_img, contours, -1, (0, 0, 255), 2)

# Annotate the number of contours on the image
cv2.putText(copy_img, f"Contours Detected: {len(contours)}", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Prepare and display images
titles = ['Original', 'Contours']
imgs = [img, copy_img]

plt.figure(figsize=(10, 5))
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
    plt.imshow(imgs[i])
plt.tight_layout()
plt.show()
