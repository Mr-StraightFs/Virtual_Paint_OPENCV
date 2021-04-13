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

ColorValues = [[51,153,255],  # The color RBG Values
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]

myPoints = []  ## Three dimentional np array with [x , y , colorId ]


def detectColor(img,Colors,ColorValues):  # Detect Color Function
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


def getContours(img):  # Define the GetContours Function : Recognizes the egdes and draw a rectangular Contour
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for ct in contours:
        area = cv2.contourArea(ct)
        if area>500:
            cv2.drawContours(imgOutput, ct, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(ct,True)
            approx = cv2.approxPolyDP(ct,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCam(myPoints, ColorValues):  # This function outputs the results on the live webcam screen
    for point in myPoints:
        cv2.circle(imgOutput, (point[0], point[1]), 10, ColorValues[point[2]], cv2.FILLED)


while True:   # Webcam Live Video Capture Loop : (Type q to stop)
    success, img = cap.read()
    if img is None or (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    cv2.imshow("Result", img)