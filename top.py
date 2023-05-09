# https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123

import cv2
import numpy as np
import matplotlib.pyplot as plt
from gau import gaussian_kernel
from scipy import ndimage
from sobel import sobel_filters, sobel_filters2
from nonmax import non_max_suppression

img = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (320, 480))
img = np.array(img).reshape(480,320,1)
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('origin')

# gaussian
gau = gaussian_kernel(5, sigma=3.0)
gau = gau.reshape(5,5,1)
img = ndimage.convolve(img,gau)

# sobel
img1, theta1 = sobel_filters(img)
img2, theta2 = sobel_filters2(img)

# non max suppression
img1 = non_max_suppression(img1, theta1)
img2 = non_max_suppression(img2, theta2)

plt.subplot(1,3,2)
plt.imshow(img1, cmap='gray')
plt.title('y/x')

plt.subplot(1,3,3)
plt.imshow(img2, cmap='gray')
plt.title('x/y')

plt.show()