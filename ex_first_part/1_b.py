import cv2 as cv

img = cv.imread('test.jpg')

cv.imwrite('test.bmp', img)
