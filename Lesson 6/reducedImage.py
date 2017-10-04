import math
import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread("img.jpg",0)
img = cv2.imread("test.jpg",0)
img_sobel64Fx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 3)
# img_sobel64Fx = np.uint8(np.absolute(img_sobel64Fx))
img_sobel64Fy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 3)
# img_sobel64Fy = np.uint8(np.absolute(img_sobel64Fy))

ht = img.shape[:2][0]
wd = img.shape[:2][1]

for i in range(ht):
    for j in range(wd):
        img[i][j] = math.sqrt(img_sobel64Fy[i][j]*img_sobel64Fy[i][j] + img_sobel64Fx[i][j]*img_sobel64Fx[i][j])

img = np.uint8(np.abs(img))
# cv2.imshow("Edge Detection At x axis!",img_sobel64Fx)
# cv2.imshow("Edge Detection At y axis!",img_sobel64Fy)
cv2.imshow("Edge Detection!",img)
# cv2.imshow("Edge Detection at work with Laplacian!",cv2.Laplacian(img,cv2.CV_64F))

cv2.waitKey(0)
cv2.destroyAllWindows()
