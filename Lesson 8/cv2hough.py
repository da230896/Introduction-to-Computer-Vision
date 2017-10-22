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
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho

    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*a)
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*a)

    cv2.line(img,(x1,y1),(x2,y2),(0,255,0))

cv2.imshow("Internal Function",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# astonishingly hough.py was somehow better than library function.