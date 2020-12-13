import cv2
import numpy as np

img = cv2.imread('lenna.png', 0)
h, w = img.shape[:2]
def canny(n=10):
    edges = cv2.Canny(img, n, n*3)
    empty = np.zeros((h, w), dtype=np.uint8)
    empty[:,:] = 255
    for i in range(0, len(edges), 1):
        for j in range(0, len(edges[i]), 1):
            if edges[i, j] == 255:
                cv2.circle(empty, (j,i), 3, int(img[i, j])+20,-1,cv2.LINE_AA)
    res = np.hstack((img,empty))
    cv2.imshow('img', res)
    cv2.imwrite('lennapont.png', res)

cv2.namedWindow("canny", 1)
cv2.createTrackbar('Canny', 'canny', 10, 200, canny)
cv2.waitKey()
