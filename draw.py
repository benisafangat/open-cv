import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

"""
img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)
"""

# 1. Point the image a certain colour

blank[:] = 0,255,0
cv.imshow('Green', blank)

blank[:] = 0,0,255
cv.imshow('Red', blank)

blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)


# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=1 )#cv.FILLED or -1
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,100), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello World!', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)