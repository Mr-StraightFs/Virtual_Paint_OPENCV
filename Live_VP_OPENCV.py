import cv2
import numpy as np

# set up the video window frame's size
frameWd = 640
frameHeight = 480
cap = cv2.VideoCapture(0)  # Set u the video capture speed
cap.set(3, frameWd)
cap.set(4, frameHeight)
cap.set(10,100)           # set up the brightness level

# The following measures are based on Min/Max hue , Min/Max Saturation
# and Min/Max Value resectively
# for the specifics of these measures please check my color detection repository :
Colors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255],
            [90,48,0,118,255,255]]
# The color RBG Values , respectively :
ColorValues = [[51,153,255],
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]

myPoints = []  ## Three dimentional np array with [x , y , colorId ]


# Webcam Live Video Capture Loop : (Type q to stop)
while True:
    success, img = cap.read()
    if img is None or (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    cv2.imshow("Result", img)