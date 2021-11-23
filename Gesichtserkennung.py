import cv2
import numpy as np


cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)



while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break 
    


