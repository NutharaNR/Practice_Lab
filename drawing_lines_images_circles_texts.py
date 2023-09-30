import cv2

cap = cv2.VideoCapture('./assets/butterfly.mp4')

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    # line(<source_img>, starting_position(x1,y1), ending_position(x2,y2), color(R,G,B), line_thickness)
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)

    # drawing rectangles, circles
    # gives top-left and bottom-right coordinates
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)  # -1 for thickness will fill the whole shape
    # radius and center is given
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    # drawing texts
    # definig the font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # the text, the position of the text need to be displayed, font, font_scale(the size of the text), color, thickness,line_type   is given
    img = cv2.putText(img, 'Butterfly', (200,height-50), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow('frame', img)

    if cv2.waitKey(100) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



