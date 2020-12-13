import numpy as np
import cv2
from matplotlib import pyplot as plt

# Carrega a imagem
img = cv2.imread('../Imagens/bolhas.png',0)
h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
img2 = img.copy()

#retira qualquer objeto nos cantos da imagem 
for i in range(0, w, 1):
    if img[0,i] != 0:
        cv2.floodFill(img, mask, (i,0), 0)

for i in range(0, w, 1):
    if img[h-1,i] != 0:
        cv2.floodFill(img, mask, (i,h-1), 0)

for i in range(0, h, 1):
    if img[i,0] != 0:
        cv2.floodFill(img, mask, (0,i), 0)

for i in range(0, h, 1):
    if img[i,w-1] != 0:
        cv2.floodFill(img, mask, (w-1,i), 0)

cv2.imwrite('labeling0.png', img)
contador = 0
for i in range(0, h, 1):
    for j in range(0, w, 1):
        if img[i,j] == 255:
            contador+=1
            cv2.floodFill(img, mask, (j,i), contador%254)
print(contador)

# conta o numero de objetos que contem furos
contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contador2 =0
for i in range(len(contours)):
    if hierarchy[0][i][2] !=-1:
        contador2+=1
        
print(contador2)
cv2.imwrite('labeling1.png', img)

cv2.waitKey(0)