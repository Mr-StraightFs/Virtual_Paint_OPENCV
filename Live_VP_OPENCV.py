import cv2
import numpy as np

class ColorDetector:
    def __init__(self):
        self.frame_width = 640
        self.frame_height = 480
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.frame_width)
        self.cap.set(4, self.frame_height)
        self.cap.set(10, 100)
        self.colors = [[5,107,0,19,255,255],
                       [133,56,0,159,156,255],
                       [57,76,0,100,255,255],
                       [90,48,0,118,255,255]]
        self.color_values = [[51,153,255],
                             [255,0,255],
                             [0,255,0],
                             [255,0,0]]
        self.points = []

    def detect_color(self, img):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        new_points = []
        for i, color in enumerate(self.colors):
            lower = np.array(color[:3])
            upper = np.array(color[3:])
            mask = cv2.inRange(img_hsv, lower, upper)
            x, y = self.get_contours(mask)
            cv2.circle(img_output, (x, y), 15, self.color_values[i], cv2.FILLED)
            if x != 0 and y != 0:
                new_points.append([x, y, i])
            cv2.imshow(str(color[0]), mask)
        return new_points

    def get_contours(self, img):
        contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        x, y, w, h = 0, 0, 0, 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                cv2.drawContours(img_output, contour, -1, (255, 0, 0), 3)
                perimeter = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
                x, y, w, h = cv2.boundingRect(approx)
        return x + w // 2, y

    def draw_on_cam(self):
        for point in self.points:
            cv2.circle(img_output, (point[0], point[1]), 10, self.color_values[point[2]], cv2.FILLED)

if __name__ == "__main__":
    detector = ColorDetector()
    while True:
        success, img = detector.cap.read()
        if img is None or (cv2.waitKey(1) & 0xFF == ord('q')):
            break
        img_output = img.copy()
        new_points = detector.detect_color(img)
        if new_points:
            detector.points.extend(new_points)
        if detector.points:
            detector.draw_on_cam()
        cv2.imshow("Result", img_output)
