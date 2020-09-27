import cv2
import numpy as np

cam = cv2.VideoCapture(0)

lower_color = (10, 150, 110)
upper_color = (50, 210, 220)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        raise ValueError('No video')

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        max_cnt = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(max_cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

        rect = cv2.minAreaRect(max_cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
