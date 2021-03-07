import cv2
import numpy as np

img = cv2.imread("img/chess.jpg",1)# 0 for grayColor 1 for colored Image and -1 for actual colored image
img2=cv2.resize(img,(400,400))

cv2.imshow('Image with Actual Size',img)

cv2.waitKey(0)
cv2.destroyAllWindows()