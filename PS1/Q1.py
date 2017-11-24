import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("box.jpg",0)
edges = cv2.Canny(img,100,100)

for i in range(edges.shape[0]):
    for j in range(edges.shape[1]):
        if edges[i][j] > 250 :
            edges[i][j] = 255
        else:
            edges[i][j] = 0

cv2.imshow("Binary Image",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
