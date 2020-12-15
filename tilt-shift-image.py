import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def count(x):
    x = x+1

cv2.namedWindow('tiltshift')

cv2.createTrackbar('Alfa', 'tiltshift', 0, 100, count)
cv2.createTrackbar('Center', 'tiltshift', 0, 100, count)
cv2.createTrackbar('Height', 'tiltshift', 0, 100, count)
bg = cv2.imread('./Imagens/ts.jpg')
img = cv2.imread('./Imagens/ts1.jpg')

width = int(cap.get(3))
height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(
    'M', 'J', 'P', 'G'), 10, (width, height))
bg = cv2.resize(bg, (width, height))

while True:
    alfaS = cv2.getTrackbarPos('Alfa', 'tiltshift')
    centerS = cv2.getTrackbarPos('Center', 'tiltshift')
    heightS = cv2.getTrackbarPos('Height', 'tiltshift')

    p1 = (max(0, int((centerS-heightS/2.0)/100.0*height)), 0)
    p2 = (min(height-1, int((centerS+heightS/2.0)/100.0*height)), width-1)

    imgTop = bg.copy()
    imgTop[p1[0]:p2[0], p1[1]:p2[1], :] = img.copy()[p1[0]:p2[0],
                                                       p1[1]:p2[1], :]
    blended = cv2.addWeighted(bg, float(
        alfaS/100), imgTop, 1-float(alfaS/100), 0)

    cv2.imshow('tiltshift', blended)
    out.write(blended)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

