import numpy as np
import cv2

img = cv2.imread('bebe.png',0)
h, w = img.shape[:2]
mx, my = int(w/2), int(h/2)

for i in range(0, mx, 1):
    for j in range(0, my, 1):
        aux = img[i][j]
        img[i][j] = img[mx + i][my + j]
        img[mx + i][my + j] = aux

for i in range(mx, w, 1):
    for j in range(0, my, 1):
        aux = img[i][j]
        img[i][j] = img[i-mx][my + j]
        img[i-mx][my + j] = aux


cv2.imwrite('trocaregioes.png', img)
cv2.waitKey(0)
