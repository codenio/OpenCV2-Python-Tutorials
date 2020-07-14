import cv2

# read the image
img = cv2.imread('slanting-cards.png')

# convert image into grey scale for thresholding
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create a named window for adding trackbars
cv2.namedWindow('Threshold Filter')

# create a dummy callback function for the trackbar
def dummy(a):
    pass

# create required trackbar using cv2.createTrackbar() 
cv2.createTrackbar("Thres Min", "Threshold Filter", 0, 255, dummy)
cv2.createTrackbar("Thres Max", "Threshold Filter", 255, 255, dummy)

while True:
    
    # read current trackbar position using cv2.getTrackbarPos() 
    tmin = cv2.getTrackbarPos("Thres Min", "Threshold Filter")
    tmax = cv2.getTrackbarPos("Thres Max", "Threshold Filter")
    
    # apply threshold to the image using the postions specified in the trackbars
    _, threshold = cv2.threshold(grey, tmin, tmax, cv2.THRESH_BINARY)
    
    # update the threshold image 
    cv2.imshow("Threshold Filter", threshold)
    
    # sense key for program termination
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# destory all open windows 
cv2.destroyAllWindows()
