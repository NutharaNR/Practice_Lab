import numpy as np
import cv2

img = cv2.imread('./assets/Chess_Board.png')
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)


# turn in to greyscale
# cz it is easier for the algorithm to detect corners in greyscale than in RGB
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# corner detection
# param - goodFeaturesToTracking(source_img, num_best_corners_to_detect, min_quality_for_the_corner(0-1), min_euclidian_distance_between_two_corners)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10)
# print(corners)

corners = np.int0(corners)

# removing the unwanted dimensionality
for i in corners:
    x, y = i.ravel()  # ravel will flatten an array [[[1,2,3]]] --> [1,2,3]
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)
cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

