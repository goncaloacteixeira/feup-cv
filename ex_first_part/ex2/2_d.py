import cv2 as cv
import numpy as np

img = cv.imread('greyscale.jpg')

nRows, nCols, nChannels = img.shape

if nChannels > 1:
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

nNoisePixels = int(nRows * nCols * 0.1)

for _ in range(nNoisePixels):
    row, col = (np.random.randint(0, nRows), np.random.randint(0, nCols))
    intensity = img[row, col]
    if intensity > 128:
        img[row, col] = 0
    else:
        img[row, col] = 255

cv.imshow("Image", img)
cv.imwrite("../noisy.jpg", img)

cv.waitKey(0)

cv.destroyAllWindows()
