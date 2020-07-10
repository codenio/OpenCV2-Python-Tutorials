import cv2

videoCapture = cv2.VideoCapture(0)

success, frame = videoCapture.read()
while success:  # Loop until there are no more frames.
    success, frame = videoCapture.read()
    # display the feed in screen
    cv2.imshow("Faces found", frame)
    # listen for user input and perform corresponding actions
    key = cv2.waitKey(1)
    if key == ord('q') or key == ord('Q'):
        break
