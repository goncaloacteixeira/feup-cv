import cv2 as cv

img = cv.imread('test.jpg')

(blueChannel, greenChannel, redChannel) = cv.split(img)

cv.imshow('Blue Channel', blueChannel)
cv.imshow('Green Channel', greenChannel)
cv.imshow('Red Channel', redChannel)

cv.waitKey(0)
cv.destroyAllWindows()

redChannel += 50

img = cv.merge([blueChannel, greenChannel, redChannel])

cv.imshow('Merged Image', img)
cv.waitKey(0)

cv.destroyAllWindows()