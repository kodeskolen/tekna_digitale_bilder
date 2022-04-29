# -*- coding: utf-8 -*-

"""
This script reads in an image from its relative path
and uses matplotlib to plot the image.

Note: The relative path uses ".." to move up
one folder, as we are in the example_scripts, but want
access to the img folder.
"""

from skimage import io
import matplotlib.pyplot as plt

img = io.imread("../img/chest_006.png")
img2 = io.imread("../img/brain_tumors/glioma3.jpg")
print(img2.shape)

plt.subplot(1, 3, 1)
plt.imshow(img2[:, :, 0])
plt.subplot(1, 3, 2)
plt.imshow(img2[:, :, 1])
plt.subplot(1, 3, 3)
plt.imshow(img2[:, :, 2])

plt.show()

