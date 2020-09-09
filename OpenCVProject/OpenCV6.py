# Image Stacking

import cv2 as cv
import numpy as np

img = cv.imread("project_folder/Screenshot.png")


imghori=np.hstack((img,img,img))
imgverti=np.vstack((img,img))
#cv.imshow("Horizonal Stacks",imghori)
#cv.imshow("Vertical Stacks",imgverti)

'''
but image showld be in same colur RGB and Blurred or Gray is not supported
imghori=np.hstack((img,img,cv.cvtColor(img,cv.COLOR_BGR2GRAY)))
 will not work here in this case as input array having diiferent size
print(img.shape) (242, 211, 3)  3 channesls means 3 colurs
print(cv.cvtColor(img,cv.COLOR_BGR2GRAY).shape) (242, 211)
1. Image Channels
A coloured and grey scale image have 3 and 1 channels respectively. 
You cannot just combine their respective matrices together so you need to convert one to the other.
With this code, I converted the grey scale to a coloured one to facilitate the combination
2. Image Sizes
It goes without saying that this method fails when you have images of different sizes. 
Why? Because you are trying to perform operations on matrices of different dimensions.
'''

grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# Make the grey scale image have three channels
grey_3_channel = cv.cvtColor(grey, cv.COLOR_GRAY2BGR)

numpy_vertical = np.vstack((img, grey_3_channel,img))
numpy_horizontal = np.hstack((img, grey_3_channel,img))

numpy_vertical_concat = np.concatenate((img, grey_3_channel,img), axis=0)
numpy_horizontal_concat = np.concatenate((img, grey_3_channel,img), axis=1)

cv.imshow('Numpy Vertical Concat', numpy_vertical_concat)
cv.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)


cv.waitKey(0)
cv.destroyAllWindows()
