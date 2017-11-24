import cv2
import numpy as np
from math import cos
from math import sin
from math import floor
from math import pi
from matplotlib import pyplot as plt
from itertools import combinations
import heapq

def process(points):
    return max(
        combinations(points, 2),
        key=lambda (a,b): (a[0] - b[0])**2 + (a[1] - b[1])**2
    )

INT_MIN = -2147483648

img = cv2.imread("ps1-input1.png",0)
smooth_img = cv2.GaussianBlur(img,(9,9),0)
edge_img = cv2.Canny(smooth_img,100,100)

# cv2.imshow("edgeImage",edge_img)

d = edge_img.shape[1]
theta = 180

H = np.zeros((2*d+1,theta+1))
Points = dict()

for i in range(edge_img.shape[0]):
    for j in range(edge_img.shape[1]):
        if edge_img[i][j] > 250:
            for k in range(181):
                D = floor(i*cos(k*pi/180) - j*sin(k*pi/180))
                if D < 0.0:
                    D += d
                H[D][k] += 1.0
                if Points.has_key((D,k)) == False:
                    Points[(D,k)] = list()
                Points[(D,k)].append((i,j))    
# only 20 lines
Heap = [(INT_MIN,-1,-1,)]*20
# Min Heap by default
for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if Heap[0][0] < H[i][j]:
            heapq.heappop(Heap)
            heapq.heappush(Heap,(H[i][j],i,j,))


Lines = list()
for x in Heap:
    if x[0] != INT_MIN:
        possible_points = Points[(x[1],x[2])]
        Lines.append(process(possible_points))

cv2.imshow("without hough lines",img)

for segment in Lines:
    cv2.line(img,(segment[0][1],segment[0][0]),(segment[1][1],segment[1][0]),(0,255,0))

cv2.imshow("Hough Fitting of Line",img)
cv2.imshow("Hough Array",np.uint8(H))
cv2.waitKey(0)
cv2.destroyAllWindows()

