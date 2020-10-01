import cv2
import numpy as np

img = cv2.imread('opencv/Photos/rubiksCube.jpg')
karnel = np.ones((5,5), np.uint8)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, karnel, iterations=1)
imgEroded = cv2.erode(imgDialation, karnel, iterations=1)


cv2.imshow("Original Image",img)
cv2.imshow("Canny Image",imgCanny)

cv2.waitKey(0)
