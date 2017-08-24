import cv2
import random
import numpy as np

def sp_noise(img,prob):
# add salt and pepper noise to image
# 'prob' is the probability(2*prob) that pixel is adulterated
    thres = 1 - prob
    output  = np.zeros(img.shape,np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # for k in range(img.shape[2]):
            rndn = random.random()
            if rndn < prob:
                output[i][j] = 0
            elif rndn > thres:
                output[i][j] = 255
            else:
                output[i][j] = img[i][j]
    return output

image = cv2.imread('bell.jpg',0)
image = sp_noise(image,0.005)

cv2.imshow('image with salt and pepper noise',image)

cv2.imshow('image after median filtering',cv2.medianBlur(image,5))

cv2.waitKey(0)
cv2.destroyAllWindows()
