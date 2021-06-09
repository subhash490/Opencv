import cv2
import numpy 
photo=numpy.zeros((720,1080,3))
photo[:,1:]=[255,255,255]
photo[1:2,:]=[0,0,0]
photo[240:241,:]=[0,0,0]
photo[480:481,:]=[0,0,0]

photo[1:240,1:]=[51,153,255]
photo[482:,1:]=[19,136,8]

photo= photo.astype(numpy.uint8)
img =cv2.imread("india-flag.png")
img=img[250:480,430:650]
photo[250:480,430:650]=img
cv2.imshow("Img",photo)
cv2.waitKey()
cv2.destroyAllWindow()
