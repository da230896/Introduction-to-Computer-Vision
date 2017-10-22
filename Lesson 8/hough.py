import cv2
import numpy as np
import heapq
from math import sin
from math import cos
from math import pi
from math import sqrt
from math import floor
from itertools import combinations
from matplotlib import pyplot as plt

INT_MIN = -2147483648

def process(points):
    return max(
        combinations(points, 2),
        key=lambda (a,b): (a[0] - b[0])**2 + (a[1] - b[1])**2
    )

real_img = cv2.imread("painting.jpg")
img = cv2.imread("painting.jpg",0)
img = cv2.Canny(img,100,100)

d = img.shape[1]
theta = 180

H = np.zeros((2*d+1,theta+1,3))
Points = dict()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] > 250:
            for k in range(181):
                D = floor(i*cos(k*pi/180) - j*sin(k*pi/180))
                if D < 0.0:
                    D += d
                H[D][k][0] += 1.0
                if Points.has_key((D,k)) == False:
                    Points[(D,k)] = list()
                Points[(D,k)].append((i,j))    

# Maximum peaks I am taking is 50 : thus maintain a minHeap of size 100
# setting threshold is also one way to improve,Farthest point algo is still not clear so O(n^2)

Heap = [(INT_MIN,-1,-1,0)]*100
heapq.heapify(Heap)

for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if Heap[0][0] < H[i][j][0]:
            heapq.heappop(Heap)
            heapq.heappush(Heap,(H[i][j][0],i,j,0,))

Lines = list()
for x in Heap:
    if x[0] != INT_MIN:
        H[x[1]][x[2]][0] = 0
        H[x[1]][x[2]][2] = 255 
        possible_points = Points[(x[1],x[2])]
        Lines.append(process(possible_points))


for segment in Lines:
    cv2.line(real_img,(segment[0][1],segment[0][0]),(segment[1][1],segment[1][0]),(0,255,0))

cv2.imshow("Hough Fitting of Line",real_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# So origin will be our top left most corner 
# co ordinate system for drawing line will be not array like 
