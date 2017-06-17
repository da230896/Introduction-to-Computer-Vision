import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('Cycle.png',-1)
img = cv2.imread('Fruit.jpg')
#out of bond cropping

# cropped = img[109:320,400:550]

print img.shape[:2]

# cv2.imshow('Cropped Image',cropped)
# cv2.imshow('Real Image',img)

img_red = img[:,:,2]
cv2.imshow('Red Image',img_red)

plt.plot(img_red[100:150])
cv2.imshow('For Plot',img_red[100:150])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

