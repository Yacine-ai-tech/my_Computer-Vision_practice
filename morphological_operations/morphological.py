import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to image
imgpath = "cameraman.tif"
img = cv2.imread(imgpath, 0)

# Kernel size and iterations as parameters
kernel_size = (5, 5)
iterations = 2
k = np.ones(kernel_size, np.uint8)

# Morphological operations
erosion = cv2.erode(img, k, iterations=iterations)
dilation = cv2.dilate(img, k, iterations=iterations)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)

# Titles for the subplots
titles = ['Original', 'Erosion', 'Dilation', 'Gradient']
imgs = [img, erosion, dilation, gradient]

# Create the plot for the morphological operations
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.ravel()

for i in range(4):
    axes[i].imshow(imgs[i], cmap='gray')
    axes[i].set_title(titles[i])
    axes[i].axis('off')  # Turn off axis

# Adjust layout for better spacing and display
plt.tight_layout()
plt.show()

# Optionally save the result images
cv2.imwrite('erosion_result.tif', erosion)
cv2.imwrite('dilation_result.tif', dilation)
cv2.imwrite('gradient_result.tif', gradient)
