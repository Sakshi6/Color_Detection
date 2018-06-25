#!usr/bin/python
import cv2,time
#reading image
img=cv2.imread('red.jpeg')
#checking shape
print img.shape
#printing data
print img
#extracting red color
onlyred=cv2.inRange(img,(0,0,0),(40,40,255))
cv2.imshow('red',img)
cv2.imshow('onlyred',onlyred)
cv2.waitKey(0)
cv2.destroyAllWindows()


