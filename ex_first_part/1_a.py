import cv2 as cv

img = cv.imread('test.jpg')

cv.imshow('test.jpg', img)
cv.waitKey(0)

print('Height: {}px\nWidth: {}px'.format(img.shape[0], img.shape[1]))