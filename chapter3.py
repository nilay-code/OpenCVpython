import cv2
import numpy as np

img = cv2.imread("Resources/lambo.jpg")
print(img.shape)
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)
imgCrop = img[0:200, 200:500]

cv2.imshow("image", img)
cv2.imshow("resize", imgResize)
cv2.imshow("crop", imgCrop)
cv2.waitKey(0)