import cv2 as cv

img = cv.imread('../ex2/test.jpg')
first = True
top_left = (0, 0)
bottom_right = (0, 0)


def export_roi():
    global top_left, bottom_right, img
    roi = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    cv.imwrite('../roi.jpg', roi)
    print("ROI Created on roi.jpg!")


def mouse_event(event, x, y, flags, params):
    global first, top_left, bottom_right
    if event == cv.EVENT_LBUTTONUP:
        if first:
            top_left = (x, y)
            first = False
        else:
            if x < top_left[0] or y < top_left[1]:
                print("Invalid Point, select another one!")
                return
            bottom_right = (x, y)
            first = True
            export_roi()


cv.imshow("Computer Vision - Ex1 d", img)

cv.setMouseCallback('Computer Vision - Ex1 d', mouse_event)

cv.waitKey(0)
cv.destroyAllWindows()
