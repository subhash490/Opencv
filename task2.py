import cv2
img_virat=cv2.imread("vi.png")
img_rohit=cv2.imread("ro.png")
img_virat1=img_virat.copy()
b=img_rohit[10:250,450:600]
a=img_virat[10:250,200:350]
img_virat[10:250,200:350]=b
img_rohit[10:250,450:600]=img_virat1[10:250,200:350]
cv2.imshow("Img",img_rohit)

cv2.waitKey()
cv2.imshow("Img",img_virat)

cv2.waitKey()
cv2.destroyAllWindow()
