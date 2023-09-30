import cv2



# show an image
img = cv2.imread('./assets/elephants.jpg', -1)

# by default format is RGB
# -1, cv2.IMREAD_COLOR : loads a color image. any tranparency of image will be meglected. It is the default flag
# 0, cv2.IMREAD_GRAYSCALE : loads image in grayscale mode
# 1 cv2.IMREAD_UNCHANGED : loads image as such including alpha channel

cv2.imshow('Image', img)
cv2.waitKey(0)      #wait infinity amount of time till a key is pressed and move to the next command.
                    # if 5--> waits 5 secs, not pressed a key, then automatically move to the next command.
cv2.destroyAllWindows()

#resize,rotate an image

img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# write an image
cv2.imwrite('./assets/new_img.jpg',img)