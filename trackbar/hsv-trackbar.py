import cv2
import numpy as np

# read the image
img = cv2.imread('toy.jpg')

# resize the image if required
img = cv2.resize(img, (500, 500))

# convert image into grey scale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert image from BGR to HSV scale
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# create a named window for add trackbar
cv2.namedWindow('HSV Filter')

# create a dummy callback function for the trackbar
def dummy(a):
    pass

# create required trackbar using cv2.createTrackbar() 
cv2.createTrackbar("Hue Min", "HSV Filter", 0, 179, dummy)
cv2.createTrackbar("Saturation Min", "HSV Filter", 0, 255, dummy)
cv2.createTrackbar("Value Min", "HSV Filter", 0, 255, dummy)
cv2.createTrackbar("Hue Max", "HSV Filter", 179, 179, dummy)
cv2.createTrackbar("Saturation Max", "HSV Filter", 255, 255, dummy)
cv2.createTrackbar("Value Max", "HSV Filter", 255, 255, dummy)

while True:
    # read current trackbar position using cv2.getTrackbarPos()
    hmin = cv2.getTrackbarPos("Hue Min", "HSV Filter")
    hmax = cv2.getTrackbarPos("Hue Max", "HSV Filter")
    smin = cv2.getTrackbarPos("Saturation Min", "HSV Filter")
    smax = cv2.getTrackbarPos("Saturation Max", "HSV Filter")
    vmin = cv2.getTrackbarPos("Value Min", "HSV Filter")
    vmax = cv2.getTrackbarPos("Value Max", "HSV Filter")

    # create lower bound and upper bound of the mask
    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])
    
    # create mask using cv2.inRange for filtering HSV  
    mask = cv2.inRange(hsv, lower, upper)
    
    # filter the image using cv2.bitwise_and() and mask 
    result = cv2.bitwise_and(img, img, mask=mask)

    # update the result
    cv2.imshow("HSV Filter", result)
    
    # sense key for program termination
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# destory all open windows
cv2.destroyAllWindows()
