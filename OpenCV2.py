import cv2
import numpy as np

img = cv2.imread("img/ironman.jpg",0)# 0 for grayColor 1 for colored Image and -1 for actual colored image

img2 = cv2.imread("img/ironman.jpg",-1)

# print(img.show)

for i in range(0,800):
    for j in range(0,800):
        img[i][j] = 255-img[i][j]

print(type(img2[0][0]))
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if img2[i][j][0]<20 and img2[i][j][1]<20 and img2[i][j][2]<20:
            for k in range(len(img2[i][j])):
                img2[i][j][k]=255       
            

cv2.imshow('IronMan  BAlck and WhiteImage',img)
cv2.imshow('IronMan colored Iamge',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()