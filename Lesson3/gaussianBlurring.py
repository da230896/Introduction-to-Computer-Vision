import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('saturn.jpg',0)

cv2.imshow('Without Noise',img)

img += (np.random.normal(size=img.shape[:2])*10).astype('uint8')

cv2.imshow('Spoiled Image',img)

cv2.imshow('Noise Reduction by Gaussian filter',cv2.GaussianBlur(img,(31,31),0))

cv2.waitKey(0)
cv2.destroyAllWindows()

# more sigma increases the noise if we are adding noise
# But more sigma decreases the noise if we are doing gaussian filter.

# With filtering you might also scale the intensities