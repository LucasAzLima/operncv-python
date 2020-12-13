import numpy as np
import cv2

img = cv2.imread('bebe.png',0)
h, w = img.shape[:2]

print("por favor, digitar uma coordenada dentro do limine, onde x =",w," e y =", w)
while(1):
    x1 = int(input("x1="))
    if x1 < 0 or x1 > w :
        print("valor errado, digitar novamente")
    else:
        break

while(1):
    y1 = int(input("y1="))
    if y1 < 0 or y1 > h :
        print("valor errado, digitar novamente")
    else:
        break
while(1):
    x2 = int(input("x2="))
    if x2 < 0 or x2 > w:
        print("valor errado, digitar novamente")
    else:
        break

while(1):
    y2 = int(input("y2="))
    if y2 < 0 or y2 > h:
        print("valor errado, digitar novamente")
    else:
        break

for i in range(y1, y2, 1):
    for j in range(x1, x2, 1):
        img[i][j] = 255 - img[i][j]

cv2.imwrite('regions.png', img)
cv2.waitKey(0)
