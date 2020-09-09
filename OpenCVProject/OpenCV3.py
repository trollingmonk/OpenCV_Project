import cv2 as cv
import numpy as np

img=cv.imread("project_folder/IMG-640x480.jpg")

cv.imshow("Picture",img)
print(img.shape)

imgcropped = img[10:100,30:300]  ## pixcel ranges
cv.imshow("CroppedPicture",imgcropped)

imgresized = cv.resize(img,(320,240)) ## Lengths X Width
cv.imshow("ResizedPicture",imgresized)
print(imgresized.shape)

cv.waitKey(0)