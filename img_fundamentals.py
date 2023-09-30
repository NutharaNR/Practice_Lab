import cv2
import random
img = cv2.imread('./assets/elephants.jpg', -1)

# print(img)
# img is represented as an array with pixel values
# print(img[256][25]) , value of one pixel

for i in range(100):
    for j in range (img.shape[1]):
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('./assets/elephants.jpg', -1)
tag = img[500:700,600:900]  # slicing the image
img[100:300,400:700] = tag
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




