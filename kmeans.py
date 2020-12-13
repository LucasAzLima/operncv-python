import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('sushi.jpg')
h, w = img.shape[:2]
Z = np.zeros((h*w, 3))
Image = np.zeros((h, w, 3), dtype=np.uint8)
Z = np.float32(Z)
bgrImage = cv.split(img)
size = (w, h) 
result = cv.VideoWriter('filename.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, size) 

for y in range(0, h, 1):
    for x in range(0, w, 1):
        for z in range(3):
            Z[y +x*h][z] = bgrImage[z][y][x]

criteria = (cv.TermCriteria_MAX_ITER | cv.TermCriteria_EPS, 10000, 0.0001)

for i in range(10):
    ret,label,center=cv.kmeans(Z,8,None,criteria,1,cv.KMEANS_RANDOM_CENTERS)
    for y in range(0, h, 1):
        for x in range(0, w, 1):
            indice = label[y +x*h][0]
            Image[y][x][0] = int(center[indice][0])
            Image[y][x][1] = int(center[indice][1])
            Image[y][x][2] = int(center[indice][2])
    # cv.imwrite('sushi/img{}.png'.format(i), Image)
    result.write(Image)

result.release()
cv.waitKey()
