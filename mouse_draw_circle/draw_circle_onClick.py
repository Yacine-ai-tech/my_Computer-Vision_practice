import cv2
import numpy as np

# Create a black image
black_image = np.zeros((512, 512, 3), np.uint8)

# Function to draw circles when left mouse button is clicked
def draw_circles(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(black_image, (x, y), 40, (255, 255, 255), -1)

# Create a named window
cv2.namedWindow('Interactive Drawing')
cv2.setMouseCallback('Interactive Drawing', draw_circles)

while True:
    cv2.imshow('Interactive Drawing', black_image)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
        break

cv2.destroyAllWindows()
