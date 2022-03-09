import cv2 as cv

img = cv.imread('../ex2/test.jpg')

cv.imwrite('test.bmp', img)
