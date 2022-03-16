import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", type=str, required=True, help="Image path")
ap.add_argument("-k", "--kernel", type=int, default=-1, help="Kernel Size for Sobel (1,3,5,7)")
ap.add_argument("-g", "--gaussian", action="store_true", help="Apply Gaussian Filter")
ap.add_argument("-gs", "--gaussiansize", type=int, default=3, help="Box Size for Gaussian Filter")

args = vars(ap.parse_args())

img = cv2.imread(args["image"], 0)

if args["gaussian"]:
    img = cv2.GaussianBlur(img, (args["gaussiansize"], args["gaussiansize"]), 0)


gX = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=args["kernel"])
gY = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=args["kernel"])
# the gradient magnitude images are now of the floating point data
# type, so we need to take care to convert them back a to unsigned
# 8-bit integer representation so other OpenCV functions can operate
# on them and visualize them
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

thresholdValue = 128
maxValue = 255


# callback method for trackbar value change
def onTrackbarValueChange(*args):
    global thresholdValue
    thresholdValue = args[0]
    th, result = cv2.threshold(combined, thresholdValue, maxValue, cv2.THRESH_BINARY)
    cv2.imshow("image", result)


# create window
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# create trackbar
cv2.createTrackbar("Value", "image", thresholdValue, maxValue, onTrackbarValueChange)

# call method to initialize first time
onTrackbarValueChange(thresholdValue)

while True:
    k = cv2.waitKey(10)

    # press esc on keyboard to exit
    if k == 27:
        break

# close all the opened windows
cv2.destroyAllWindows()
