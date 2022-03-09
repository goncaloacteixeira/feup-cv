import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if ret:
        cv2.imshow('recording', frame)

        k = cv2.waitKey(30)
        if k == 32:
            cv2.imshow('Captured', frame)
            break

vid.release()

cv2.destroyWindow('recording')

cv2.waitKey(0)
cv2.destroyAllWindows()