import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
kamera.set(4, 1080)
karnel = np.ones((5,5), np.uint8)

while True:
    ret,img = kamera.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
    blurCanny = cv2.Canny(imgBlur, 100, 100)
    imgCanny = cv2.Canny(img, 100, 100)

    cv2.imshow("Blur Canny",blurCanny)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        print('Closing...')
        break
kamera.release()

cv2.destroyAllWindows()

