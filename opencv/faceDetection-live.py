import cv2
import numpy as np

eyeCascade = cv2.CascadeClassifier('opencv/Resoults/haarcascade_eye.xml')
faceCascade = cv2.CascadeClassifier('opencv/Resoults/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
cam.set(4, 1080)


while True:
    ret,img = cam.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes = eyeCascade.detectMultiScale(imgGray, 1.1, 4)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Result",img)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        print("Closing...")
        break

cv2.destroyAllWindows()