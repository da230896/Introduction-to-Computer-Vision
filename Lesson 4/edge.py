# We are trying gaussian kernel over image when kernel is out of boundary

# In general there are 4 ways
# 1. Black sip in--> cv2.GaussianBlur(img,(31,31),0,cv2.BORDER_CONSTANT)            ->  creates Black Boundaries
#       for Gaussian Constant Border means value is zero and it is predefined  
# 2. Wrapping and uses logic Based on Fourier                                       ->  Opposite edge reflection
#       cv2.GaussianBlur(img,(31,31),0,cv2.BORDER_WRAP)
# 3. Replicate                                                                      ->  Does our Job
#       cv2.GaussianBlur(img,(31,31),0,cv2.BORDER_REPLICATE)
# 4. Reflect                                                                        ->  Does Our Job
#       cv2.GaussianBlur(img,(31,31),0,cv2.BORDER_REFLECT)

# Last two are most imp

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bell.jpg')

cv2.imshow('Gaussian Filter in cv2 self blur edges or Not?',cv2.GaussianBlur(img,(25,25),0,cv2.BORDER_REFLECT))

cv2.waitKey(0)
cv2.destroyAllWindows()
