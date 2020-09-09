import cv2 as cv
import numpy as np

#videocap = cv.VideoCapture("project_folder/samplevideo.mp4")
videocap = cv.VideoCapture(0) # webcam feed defaultid is 0
videocap.set(3,640) # Webcam video Resolution width defaultid is 3
videocap.set(4,480) # Webcam video Resolution height defaultid is 4
videocap.set(10,100) # Increase Webcam video brightness defaultid is 10
while True:
    success,img = videocap.read()
    cv.imshow("Video",img)
    if cv.waitKey(5) & 0xFF == ord("q"): # hit q to stop
        break