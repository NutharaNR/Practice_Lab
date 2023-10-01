import numpy as np
import cv2

img = cv2.imread('./assets/soccer.jpg', 0)  # grayscale image reading
template = cv2.imread('./assets/shoe.jpg', 0)
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
template = cv2.resize(template, (0, 0), fx=0.2, fy=0.2)

# cv2.imshow('Match', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

h, w = template.shape

# set of different methods for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    # drawing a rectangle on the image where it matches the template img

    result = cv2.matchTemplate(img2, template, method)  # returns a 2-D array in a CNN
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # returns the min, mix values and the locations.i.e. the best matching location
    # print(min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0]+w, location[1]+h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
