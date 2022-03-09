import cv2 as cv

img = cv.imread('test.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
(hue, saturation, value) = cv.split(img)

cv.imshow('Hue Channel', hue)
cv.imshow('Saturation Channel', saturation)
cv.imshow('Value Channel', value)

cv.waitKey(0)
cv.destroyAllWindows()

saturation += 50

img = cv.merge([hue, saturation, value])
img = cv.cvtColor(img, cv.COLOR_HSV2BGR)

cv.imshow('Merged Image', img)
cv.waitKey(0)

cv.destroyAllWindows()