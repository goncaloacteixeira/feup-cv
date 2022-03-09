import cv2 as cv
import numpy as np

m = np.zeros((100, 200, 3), np.uint8)
m[:] = [0, 255, 255]

cv.line(m, (0, 0), (200, 100), [255, 0, 0], 5)
cv.line(m, (200, 0), (0, 100), [0, 0, 255], 5)

cv.imshow("Colored Image", m)

cv.waitKey(0)
