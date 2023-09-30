import cv2
import numpy as np

cap = cv2.VideoCapture('./assets/butterfly.mp4')
# cap = cv2.VideoCapture(0),0,1,2,... for each webcam or any other video capturing devices

# keep displaying the video
while True:
    ret, frame = cap.read() # returns a frame of the video


    # turn the frame into an image

    width = int(cap.get(3))  # property 3 returns the width
    height = int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # cannot rotate 90, because doesn't fit the arraye dimensions when rotated
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame
    # display the frame
    cv2.imshow('frame',image)

    if cv2.waitKey(100) == ord('q'):  # going to wait 1 millsec and check if the pressed key is 'q'
        break
cap.release()  # going to release the resources
cv2.destroyAllWindows()



