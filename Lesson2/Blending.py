import cv2
import numpy as np
from matplotlib import pyplot as plt

def blend (image1,image2,alpha):
    image3 = image1*(1-alpha) + image2*alpha
    return image3

dolphin = cv2.imread('Dolphin.png',0)
cycle = cv2.imread('Cycle.png',0)

height = min(dolphin.shape[:2][0],cycle.shape[:2][0])
width = min(dolphin.shape[:2][1],cycle.shape[:2][1])

dolphin= dolphin[0:height,0:width]
cycle = cycle[0:height,0:width]

# result = blend(dolphin,cycle,0.15)
# print result[100].astype(int)
result = cv2.absdiff(dolphin,cycle)

# result = result.astype('uint8')
# plt.plot(result[100])
#print result[0][0],cycle[0][0],dolphin[0][0]

cv2.imshow('Resultant Image',result)
plt.show()

cv2.waitKey(0)
plt.close('all')
cv2.destroyAllWindows()