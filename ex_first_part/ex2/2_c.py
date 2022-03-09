import cv2 as cv

colored = cv.imread('test.jpg')
greyscale = cv.cvtColor(colored, cv.COLOR_BGR2GRAY)

cv.imshow("Colored Image", colored)
cv.imshow("Greyscale Image", greyscale)

cv.waitKey(0)

cv.imwrite('greyscale.jpg', greyscale)

cv.destroyAllWindows()
