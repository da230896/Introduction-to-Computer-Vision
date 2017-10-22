import cv2
import numpy as np
from math import pi
from matplotlib import pyplot as plt

img = cv2.imread("painting.jpg")
edge = cv2.Canny(img,100,100)
D = max(edge.shape[0],edge.shape[1])
Lines = cv2.HoughLines(edge,1,np.pi/180,115)

YMAX = img.shape[0]
XMAX = img.shape[1]

for i in Lines:
    rho,theta = i[0]
    x1 = 0
    y1 = rho/np.sin(theta)
    if y1 >= YMAX:
        y1 = YMAX-1
        x1 = (rho - y1*np.sin(theta))
    elif y1 < 0:
        y1 = 0
        x1 = rho
    y2 = 0
    x2 = rho/np.cos(theta)
    if x2 >= XMAX:
        x2 = XMAX-1
        y2 = (rho - x2*np.cos(theta))
    elif x2 < 0:
        x2 = 0
        y2 = rho

    cv2.line(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0))

cv2.imshow("Internal Function",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# astonishingly hough.py was somehow better than library function.