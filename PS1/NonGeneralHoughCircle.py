import cv2
import numpy as np
from matplotlib import pyplot as plt
import heapq
import math

INT_MIN = -2147483648

img = cv2.imread("ps1-input1.png",0)
smooth_img = cv2.GaussianBlur(img,(9,9),0)
edges_img = cv2.Canny(smooth_img,100,100)

# since center can lie outside
offset = 20
radius = 20
H = np.zeros((edges_img.shape[0] + 2*20 + 1,edges_img.shape[1] + 2*20 + 1))

# print img.shape

for i in range(edges_img.shape[0]):
    for j in range(edges_img.shape[1]):
        if edges_img[i][j] >= 250:
            for theta in range(360):
                x = int(i + radius*np.cos(theta*np.pi/180))
                y = int(j + radius*np.sin(theta*np.pi/180))
                H[x + offset][y + offset] += 1.0
# Peaks are 10
Peaks = [(INT_MIN,-1,-1)]*10

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if Peaks[0][0] < H[i][j]:
            heapq.heappop(Peaks)
            heapq.heappush(Peaks,(H[i][j],i-offset,j-offset))

for centers in Peaks:
    if centers[0] != INT_MIN:
        cv2.circle(img,(centers[2],centers[1]),radius,(0,255,0))

cv2.imshow("Specific Hough Circles",img)
cv2.imshow("Accumulator",np.uint8(H))

cv2.waitKey(0)
cv2.destroyAllWindows()