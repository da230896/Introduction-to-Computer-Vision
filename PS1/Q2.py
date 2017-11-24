import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("noisyBox.png",0)
smooth_img = cv2.GaussianBlur(img,(13,13),0)

# sigmaX and sigmaY : if both are given as zeros, they are calculated from kernel size

# edges_img = cv2.Canny(img,100,100)
edges_smooth_img = cv2.Canny(smooth_img,100,100)

# cv2.imshow("ps1-3-b-1.png",edges_img)
# cv2.imshow("ps1-3-b-2.png",edges_smooth_img)

Lines = cv2.HoughLines(edges_smooth_img,1,np.pi/180,65)
# int(0.75*min(img.shape[0],img.shape[1])) can be used since lines are image wide
# 4th argument is indication of nmber of point on line

for i in Lines:
    # print i
    rho,theta = i[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho

    x1 = int(x0 - 1000*b)
    y1 = int(y0 + 1000*a)
    x2 = int(x0 + 1000*b)
    y2 = int(y0 - 1000*a)

    cv2.line(edges_smooth_img,(x1,y1),(x2,y2),(255,255,255))

cv2.imshow("Non required",edges_smooth_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


