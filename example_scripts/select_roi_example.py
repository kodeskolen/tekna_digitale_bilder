import skimage
import cv2
import matplotlib.pyplot as plt

# Read a specific image using cv2
img = cv2.imread("img/brain_tumors/glioma5.jpg")

# Use an interactive tool for selecting the region of interest
x0, y0, dx, dy = cv2.selectROI(img)

# Perform actual cropping using slicing of numpy arrays
crop = img[y0:y0+dy, x0:x0+dx]

# Show results
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Full image')

plt.subplot(1, 2, 2)
plt.imshow(crop)
plt.title('Cropped selection')
plt.show()


