import cv2
import numpy as np

# create a blank screen using zero matrix
img = np.zeros((512, 512, 3), np.uint8)

center = int(512/2)

# draw a line using cv2.line
cv2.line(img, (512, 0), (0, 512), (0, 0, 255), 5)
# one more line
cv2.line(img, (0, 0), (512, 512), (0, 0, 255), 5)

# draw rectangle using cv2.rectangle
cv2.rectangle(img, (center - 50, center - 50 ), (center + 50, center + 50), (0, 200, 200), 2)

# draw circle using cv2.circle
cv2.circle(img, (center, center), 40, (150, 250, 100), cv2.FILLED)

# add text using cv2.putText
cv2.putText(img, "Basic Shapes", (center - 100, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

cv2.imshow('plot', img)

cv2.waitKey(0)
cv2.imwrite('shapes.jpeg', img)
cv2.destroyAllWindows()