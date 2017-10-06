import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("img.jpg",0)
img = cv2.GaussianBlur(img,(5,5),0)

# shift image left by 1 pixel 
# shift image right by 1 pixel and compute their difference
# its like [0 0 1]*I - [1 0 0 ]*I but do remeber to scale your image

left = img[:][2:]
np.append(left,img[:][-1])

right = img[:][0]
np.append(right,img[:][:-2])

final_image = (right/2 - left/2).astype('double')
final_image = np.uint8(np.abs(final_image))

cv2.imshow("First Derivative of 2D image",final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

