#%%

import numpy as np
import cv2
from matplotlib import pyplot as plt

#img  = cv2.imread('MB.jpg',1)
#img  = cv2.imread('plain.jpg')
#img = cv2.imread('Red.jpg')
img = cv2.imread('Dolphin.png',1)
# print(img.shape[:2])
# print(img[100:103,200:203])
cv2.line(img,(0,0),(img.shape[:2][1],img.shape[:2][0]),(0,255,0))
# BGR
cv2.imshow('Image',img)
plt.plot(img[50,:])
plt.ylabel('Gray Values')
plt.show()
#plt.hist(img.ravel(),256,[0,256]);plt.show();


cv2.waitKey(0)
cv2.destroyAllWindows()

#Side Notes
#img.shape[:2] gives height,width
#BGR notation 
# waitKey(time) else if 0 the it waits indefinitely
#destroyWindow(name) destroy only the frame with name
#imread : flags -- >0 3channel color image
#                  =0 Gray scale
#                  <0 Load image as is with Alpha Channel                      