import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Cycle.png',-1)

#out of bond cropping

cropped = img[109:320,400:550]

print(img.shape[:2])

cv2.imshow('Cropped Image',cropped)
cv2.imshow('Real Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

