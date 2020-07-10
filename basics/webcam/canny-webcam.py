import cv2

videoCapture = cv2.VideoCapture(0)

success, frame = videoCapture.read()
while success:  # Loop until there are no more frames.
    success, frame = videoCapture.read()
    # convert to grey scale
    canny = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    # gaussian blur the image
    canny = cv2.GaussianBlur(canny, ksize=(7, 7), sigmaX=5)
    # canny the image
    canny = cv2.Canny(canny, 50, 50)

    # display the feed in screen
    cv2.imshow("Original", frame)
    # display the canny image on the screen
    cv2.imshow("Canny", canny)
    # listen for user input and perform corresponding actions
    key = cv2.waitKey(1)
    if key == ord('q') or key == ord('Q'):
        break
