import cv2

vid = cv2.VideoCapture(0)

print('Press ESC to close the window...')

while True:
    ret, frame = vid.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # TODO HERE
        cv2.imshow('Camera', frame)

    k = cv2.waitKey(50)
    if k == 27:
        break

vid.release()
cv2.destroyAllWindows()
