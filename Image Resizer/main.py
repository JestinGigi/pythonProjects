import cv2 as cv
import numpy as np

img = cv.imread('nature.jpg')

cv.imshow("", img)
cv.waitKey(50000)
height,width = img.shape[:2]
res = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)

cv.imwrite("starry_night.png", res)