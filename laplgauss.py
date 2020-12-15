
import cv2
import sys
import numpy as np

cam = cv2.VideoCapture(0)

if (cam.isOpened() == False): 
	print("Error reading video file") 

mean= np.array([[0.1111,0.1111,0.1111],
                [0.1111,0.1111,0.1111],
                [0.1111,0.1111,0.1111]], np.float32)

gauss= np.array([[.0625,0.125,0.0625],
                [0.125,0.25,0.125],
                [0.0625,0.125,0.0625]], np.float32)     

vertical = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]], np.float32)

horizontal = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], np.float32)

laplacian = np.array([[0,-1,0],
                    [-1,4,-1],
                    [0,-1,0]], np.float32)

boost = np.array([[0,-1,0],
                [-1,5.2,-1],
                [0,-1,0]], np.float32)

mask = []
original = True
absolute = False
laplaGauss = False
while(1):
    ret, img = cam.read()
    if img is None:
        break
    k = cv2.waitKey(30) & 0xff
    if k == ord('o'):
        original = True
        
    if k == 27:
        break
    elif k == 'a':
        absolute = not absolute
        original = False
        laplaGauss = False
    elif k == ord('m'):
        mask = mean
        original = False
        laplaGauss = False
    elif k == ord('g'):
        mask = gauss
        original = False
        laplaGauss = False
    elif k == ord('h'):
        mask = horizontal
        original = False
        laplaGauss = False
    elif k == ord('v'):
        mask = vertical
        original = False
        laplaGauss = False
    elif k == ord('l'):
        mask = laplacian
        original = False
        laplaGauss = False
    elif k == ord('b'):
        mask = boost
        original = False
        laplaGauss = False
    elif k == ord('s'):
        original = False
        laplaGauss = True

    if laplaGauss:
        img = cv2.filter2D(img, -1, gauss)
        img = cv2.filter2D(img, -1, laplacian)
        cv2.imshow("Video", img)
    elif not (original):
        img = cv2.filter2D(img, -1, mask)
        cv2.imshow("Video", img)
    if absolute:
        img = cv2.abs(img)
    cv2.imshow("Video", img)
