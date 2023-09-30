import cv2
import numpy as np

cap = cv2.VideoCapture('./assets/butterfly.mp4')
while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([50, 10, 50])
    upper_blue = np.array([255, 130, 255])

    # mask returns a new image with only the pixels belong to the following range, others as (0,0,0)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # mask is only has 0s and 1s
    result = cv2.bitwise_and(frame, frame,  mask=mask)
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(100) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


