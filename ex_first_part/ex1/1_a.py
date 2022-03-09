import cv2 as cv

img = cv.imread('../ex2/test.jpg')

cv.imshow('test.jpg', img)
print('Height: {}px\nWidth: {}px'.format(img.shape[0], img.shape[1]))

print("Press any key to continue...")

cv.waitKey(0)

