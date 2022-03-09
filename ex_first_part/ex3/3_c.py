import cv2

vid = cv2.VideoCapture(0)

print('Press ESC to close the window...')

while True:
    ret, frame = vid.read()
    if ret:
        cv2.imshow('Colored Camera', frame)
        greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        th, dst = cv2.threshold(greyFrame, 128, 255, cv2.THRESH_BINARY)
        cv2.imshow('Greyscale Camera', dst)

    k = cv2.waitKey(50)
    if k == 27:
        break

vid.release()
cv2.destroyAllWindows()
