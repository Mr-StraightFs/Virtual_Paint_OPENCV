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

# Detect Color Function
def detectColor(img,Colors,ColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #Converting to the HSV color enviroment
    count = 0
    newPoints=[]
    for clr in Colors:
        lower = np.array(clr[0:3])
        upper = np.array(clr[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgOutput,(x,y),15,ColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        cv2.imshow(str(clr[0]),mask) #show mask
    return newPoints


# Webcam Live Video Capture Loop : (Type q to stop)
while True:
    success, img = cap.read()
    if img is None or (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    cv2.imshow("Result", img)