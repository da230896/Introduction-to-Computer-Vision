import cv2
import numpy as np
from matplotlib import pyplot as plt

mu,sigma = 0,1
arr = np.random.normal(mu,sigma,10000)
f,(hist1,hist2,curve) = plt.subplots(3)
count, bins, ignored = hist1.hist(arr,50,normed=True)
curve.plot(bins,1/(sigma * np.sqrt(2*np.pi)) * np.exp((-(bins-mu)**2/2*sigma**2)),color='r')
#task : try sigma*2
arr = np.multiply(arr,10)
count, bins, ignored = hist2.hist(arr,50,normed=True)

curve.plot(bins,1/(sigma * np.sqrt(2*np.pi)) * np.exp((-(bins-mu)**2/2*sigma**2)),color='b')
f.subplots_adjust(hspace=0)
plt.show()

# img = cv2.imread('Fruit.jpg')
# cv2.imshow('Without Noise',img)
# noise = np.random.normal(size=img.shape[:2]) * 50
# img += noise
# cv2.imshow('After Noise',img.astype('uint8'))

cv2.waitKey(0)
cv2.destroyAllWindows()

#We can think noise seperately
#   Now in Noise mean is the gray value i.e zero 
#   -infinite is black
#   +infinite is white
#   Now with noise having lower standard deviation 
#   gray value doest not differ much , not much 
#   sparkles

#Now if int8 then we can have -128 as min(black) and +127 as max
#so we need to take care about sigma now
#if float image of 0.0 to 1.0 or 0.0 to 255.0 then 0.5/127.5 would be gray and we nead to 
#   redefine mean of gaussian
#
#But the concept remains same that if we increase the mu
#we increase the sparkling in picture