import cv2
import numpy as np

img = cv2.imread("img/chess.jpg",0)# 0 for grayColor 1 for colored Image and -1 for actual colored image
img2=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img2 = cv2.rotate(img2,cv2.cv2.ROTATE_90_CLOCKWISE)
npArray = np.array([])
npArray = img
# print(img.show)
print(img[0][0])
for i in range(0,400):
    for j in range(0,400):
        if img[i][j]>(255/2):
            img[i][j]=0
        else:
            img[i][j]=255

cv2.imshow('Image Actual Size',img)
cv2.imshow('Image with small Size',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()