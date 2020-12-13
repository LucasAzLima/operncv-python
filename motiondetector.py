import cv2
import sys
import numpy as np

cam = cv2.VideoCapture(0)

if (cam.isOpened() == False): 
	print("Error reading video file") 
width = int(cam.get(3)) 
height = int(cam.get(4)) 

size = (width, height) 
result = cv2.VideoWriter('filename.avi', 
						cv2.VideoWriter_fourcc(*'MJPG'), 
						10, size) 

ret, img = cam.read()
Hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])

while(1):
    ret, img = cam.read()
    if ret:
        hist2 = cv2.calcHist([img], [0], None, [256], [0, 256])
        histDiff = Hist1 - hist2
        comp = cv2.compareHist(Hist1, hist2, cv2.HISTCMP_CHISQR)
        print(int(comp)/1000)
        Hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])
        if int(comp)/1000 > 5:
            cv2.rectangle(img, (0, 0), (width-1, height-1), (0, 0, 255), 10)
        cv2.imshow("Video", img)
        result.write(img) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cam.release() 
result.release() 
	
# Closes all the frames 
cv2.destroyAllWindows() 