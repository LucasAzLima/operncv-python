import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
# img = cv2.imread('exercicios/img.jpg');
while(True):
    ret, img = cap.read(0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img,equ))
    cv2.imshow('Source image', res)
    cv2.imwrite('equalize.png', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
