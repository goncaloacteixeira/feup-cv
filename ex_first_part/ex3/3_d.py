import cv2
import numpy as np

vid = cv2.VideoCapture(0)

print('Press ESC to close the window...')

while True:
    ret, frame = vid.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([100, 128, 0], dtype=np.uint8)
        upper_blue = np.array([130, 255, 255], dtype=np.uint8)

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    k = cv2.waitKey(1)
    if k == 27:
        break

vid.release()
cv2.destroyAllWindows()
