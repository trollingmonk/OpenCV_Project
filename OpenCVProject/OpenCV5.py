#Wrap Prespective

import cv2 as cv
import numpy as np

####Example 1 ####
img = cv.imread("project_folder/pyramid_of_cards.jpg")
width,height = 95,125

#Cordination points manually taken by hovering mouse over image
points1 = np.float32([[20,258] , [83,259] ,[7,347] ,[73,346]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

metrix = cv.getPerspectiveTransform(points1,points2)
imgoutput = cv.warpPerspective(img,metrix,(width,height))

cv.imshow("Orignal Pic 1",img)
cv.imshow("Extracted Image 1",imgoutput)

####Example 2 ####
img2 = cv.imread("project_folder/1200px-Hand_in.jpg")
img2 = cv.resize(img2,(300,500))
width2,height2 = 225,315  #Paying Crad dimentions (Actually its 250*350)

#Cordination points manually taken by hovering mouse over image
points11 = np.float32([[46,379] , [95,341] ,[83,463] ,[136,416]])
points22 = np.float32([[0,0],[width2,0],[0,height2],[width2,height2]])

metrix2 = cv.getPerspectiveTransform(points11,points22)
imgoutput2 = cv.warpPerspective(img2,metrix2,(width2,height2))

cv.imshow("Orignal Pic 2",img2)
cv.imshow("Extracted Image 2",imgoutput2)

cv.waitKey(0)