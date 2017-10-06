import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

froomer = cv2.imread("froomer.jpg",0)
frizzy = cv2.imread("frizzy.jpg",0)

froomer = cv2.Canny(froomer,50,50)
frizzy = cv2.Canny(frizzy,50,50)


cv2.imshow("Edge for froomer",froomer)
cv2.imshow("Edge detection for frizzy",frizzy)

# cv2.imshow("Anding images",frizzy & froomer)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
    Pretty clear Canny does better work and lesser Code :)
"""