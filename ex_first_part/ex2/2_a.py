import cv2 as cv
import numpy as np

m = np.ones((100, 200, 1), np.uint8) * 100

cv.line(m, (0, 0), (200, 100), 255, 5)
cv.line(m, (200, 0), (0, 100), 255, 5)

cv.imshow("Greyscale Image", m)

cv.waitKey(0)
