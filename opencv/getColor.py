import cv2
import numpy as np
from random import randint
import time

boolean = input('Do you want to use your webcam?\ny or n\n')
boolean = upper(boolean)

if boolean == "y": 
    boolean = True
    print("webcam will used")
if boolean == "n": 
    boolean = False
    print("photos will be used")
time.sleep("to change your colors when you on top of the picture:\nRed-r\nOrange-o\nyellow-y\ngreen-g\nblue-b")

webcam = boolean

path = 'opencv/Photos/rubiksCube.jpg'
cap = cv2.VideoCapture(0)


def setColor(inp):
    inp = int(inp)

    if inp  == 1:
        lower = red[0]
        upper = red[1]
    if inp  == 2:
        lower = orange[0]
        upper = orange[1]
    if inp  == 3:
        lower = yellow[0]
        upper = yellow[1]
    if inp  == 4:
        lower = green[0]
        upper = green[1]
    if inp  == 5:
        lower = blue[0]
        upper = blue[1]

    return lower, upper


red = np.array([[0, 50, 50], [6, 255, 255]])
orange = np.array([[10, 50, 50], [20, 255, 255]])
yellow = np.array([[20, 50, 50], [30, 255, 255]])
green = np.array([[60, 50, 50], [90, 255, 255]])
blue = np.array([[90, 50, 50], [150, 255, 255]])

r = randint(1, 5)

color = setColor(r)

while True:
    if webcam: success, img = cap.read()
    else: img = cv2.imread(path)
    

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)# HSV e çevirir
    mask = cv2.inRange(hsv, color[0], color[1])# o rengi beyaz diyerlerini siyah yapar
    kendi_rengi = cv2.bitwise_and(img, img, mask = mask)# kendi rengini gösterir diyer renkleri siyah yapar

    cv2.imshow("Original", img)
    cv2.imshow("Mask", kendi_rengi)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        print('Closing...')
        break
    
    if cv2.waitKey(1) & 0xFF==ord('r'):
        print('Red')
        color = setColor(1)
    
    if cv2.waitKey(1) & 0xFF==ord('o'):
        print('Orange')
        color = setColor(2)
    
    if cv2.waitKey(1) & 0xFF==ord('y'):
        print('Yellow')
        color = setColor(3)
    
    if cv2.waitKey(1) & 0xFF==ord('g'):
        print('Green')
        color = setColor(4)
    
    if cv2.waitKey(1) & 0xFF==ord('b'):
        print('Blue')
        color = setColor(5)


cv2.destroyAllWindows()
