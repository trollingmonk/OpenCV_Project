import cv2 as cv
import numpy as np

img = np.zeros((340,280,3),np.uint8)  # np.uint8 means 0 to 255 range
print(img.shape) # Image Metrics 3 col = 3 dimention Metrics that showed off colors

# colouring the image with Blue-Green-Red combinations (max 255 as np.zeros has 0 to 255 range)
img[:] = 155,255,200

## Lines in Image
cv.line(img,(20,57),(90,100),(0,0,255),thickness=3)  ## heigth and width in imagle pixels

# Rectanges in Image
cv.rectangle(img,(50,20),(250,200),(200,0,0),thickness=2) # start , end and colur of rectangle

# Circle in Image
cv.circle(img,(180,40),30,(0,0,200),thickness=2)

# Put Text in Image
cv.putText(img,"OpenCV Project",(100,250),cv.FONT_HERSHEY_COMPLEX_SMALL,0.95,(255,255,255),thickness=2)

cv.imshow("New image",img)
cv.waitKey(0)