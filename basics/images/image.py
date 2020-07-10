import cv2
import numpy as np

# read an image using cv2.imread
img = cv2.imread('baboon.jpg')
cv2.imshow("Actual Image", img)

# resize an image unsing cv2.resize
resized = cv2.resize(img, dsize=(200, 300))
cv2.imshow("Resized", resized)

# make grey scale of an image using cv2.cvtColor
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey', grey)

# blur an image using cv2.blur
blur = cv2.blur(grey, (7, 7))
cv2.imshow('blured', blur)

# blur an image using cv2.GaussianBlur
gaussianBlur = cv2.GaussianBlur(grey, (7, 7), 5)
cv2.imshow('gaussianBlur', gaussianBlur)

# find edges using cv2.Canny
canny = cv2.Canny(gaussianBlur, 70, 70)
cv2.imshow('canny', canny)

# dilate image using cv2.dilate
kernel = np.ones((5, 5))
dilate = cv2.dilate(canny, kernel, iterations=1)
cv2.imshow('dilated', dilate)

# erode image using cv2.erode
erode = cv2.erode(dilate, kernel, iterations=1)
cv2.imshow('eroded', erode)


cv2.waitKey(0)
cv2.imwrite('resized.jpeg', resized)
cv2.imwrite('greyed.jpeg', grey)
cv2.imwrite('blured.jpeg', blur)
cv2.imwrite('gaussian-blured.jpeg', gaussianBlur)
cv2.imwrite('canny.jpeg', canny)
cv2.imwrite('dilated.jpeg', dilate)
cv2.imwrite('eroded.jpeg', erode)


cv2.destroyAllWindows()
