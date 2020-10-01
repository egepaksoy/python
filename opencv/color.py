import cv2
import numpy as np

img = cv2.imread('opencv/Photos/rubiksCube.jpg')

lower = np.array([60, 50, 50])
upper = np.array([90, 255, 255])

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
kendi_rengi = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("Original", img)
cv2.imshow("Masked", kendi_rengi)

        
cv2.waitKey(0)