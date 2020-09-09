import cv2 as cv
import numpy as np

img =cv.imread("project_folder/sample1_mini.png")
cv.imshow("Orignal",img)

imggray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",imggray)

imgblur=cv.GaussianBlur(imggray,(5,5),0) # kernel size could only odd numbers of metrics
#cv.imshow("Blur",imgblur)

imgcanny=cv.Canny(imggray,100,150)
cv.imshow("Canny",imgcanny)

kernel= np.ones((6,6),np.uint8)

imgdialation=cv.dilate(imgcanny,kernel,iterations=1)
cv.imshow("Dialation",imgdialation)

imgeroded = cv.erode(imgdialation,kernel,iterations=1)
cv.imshow("Eroded",imgeroded)

cv.waitKey(0)