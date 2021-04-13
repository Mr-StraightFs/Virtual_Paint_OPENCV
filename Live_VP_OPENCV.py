import cv2
import numpy as np

# set up the video window frame's size
frameWd = 640
frameHeight = 480
cap = cv2.VideoCapture(0)  # Set u the video capture speed
cap.set(3, frameWd)
cap.set(4, frameHeight)
cap.set(10,100)           # set up the brightness level

# Webcam Live Video Capture Loop : (Type q to stop)
while True:
    success, img = cap.read()
    if img is None or (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    cv2.imshow("Result", img)