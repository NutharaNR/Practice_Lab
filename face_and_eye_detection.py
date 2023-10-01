import numpy as np
import cv2


# using a pretrained classification model for face recognition
cap = cv2.VideoCapture('./assets/faces.mp4')

# using haarcascade models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    # requres grayscale image to perform the classification
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # params - (source_img, scale_factor, minNeighbours)
    # scale_factor --> 1.3 --> shrink the image in each iteration by 30%
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # returns the positions of the faces in terms of locations

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)

        # eyes are within the face boundary
        # hence pass the face region to eye detector
        roi_gray = gray[y:y+h, x:x+w]
        roi_colour = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_colour, (ex, ey), (ex+ew, ey+eh), (0, 255, 0),5)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(100) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()