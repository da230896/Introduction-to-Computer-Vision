# find the left topmost co ordinate of the template in the image
import cv2
import numpy as np
from matplotlib import pyplot as plt

# img.shape[:2] produces (height,width)

def check(img,template,i,j):
    for x in range(template.shape[:2][0]):
        for y in range(template.shape[:2][1]):
            if i+x < img.shape[:2][0] and j+y < img.shape[:2][1]:
                if img[i+x][j+y] != template[x][y]:
                    return False
            else:
                return False
    return True

def find_template_2D(img,template):
    for i in range(img.shape[:2][0]):
        for j in range(img.shape[:2][1]):
            if img[i][j] == template[0][0]:
                if check(img,template,i,j):
                    return (i,j)
                else:
                    continue
    return (-1,-1)                

tb = cv2.imread('tablet.png',0)
# print tb.shape
glyph = tb[90:165,185:245]
# print glyph
# print glyph[0][0]

cv2.imshow('Tablet',tb)
cv2.imshow('glyph',glyph)

loc = find_template_2D(tb,glyph)

if loc[0] != -1 :
    print loc
else:
    print 'Template Not Found'

cv2.waitKey(0)
cv2.destroyAllWindows()