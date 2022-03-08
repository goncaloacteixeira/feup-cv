import cv2 as cv

img = cv.imread('test.jpg')
img_copy = img.copy()


def mouse_event(event, x, y, flags, params):
    global img
    img = img_copy.copy()
    if event == cv.EVENT_MOUSEMOVE:
        font = cv.FONT_HERSHEY_SIMPLEX
        b, g, r = img[y, x]
        cv.putText(img, "{},{},{}".format(r, g, b), (x, y), font, 1, (255, 0, 0), 2)
        cv.imshow('Computer Vision - Ex1 c', img)
    if event == cv.EVENT_LBUTTONUP:
        b, g, r = img[y, x]
        print('Current Value for pixel [{},{}]: RGB({},{},{})'.format(x, y, r, g, b))
        r, g, b = [int(x) for x in input('Enter new Value for this pixel [{},{}] (R,G,B):'.format(x, y)).split(',')]
        img_copy[y, x] = (b, g, r)


cv.imshow("Computer Vision - Ex1 c", img)

cv.setMouseCallback('Computer Vision - Ex1 c', mouse_event)

cv.waitKey(0)
cv.destroyAllWindows()
