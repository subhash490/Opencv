import cv2
import numpy
tiger=cv2.imread("tiger.png")
lion=cv2.imread("lion.png")
lion=lion[300:698,400:1000]
img1=numpy.hstack([tiger,lion])
img2=numpy.vstack([tiger,lion])
cv2.imshow("Img",img1)

cv2.waitKey()
cv2.imshow("Img",img2)

cv2.waitKey()
cv2.destroyAllWindow()
