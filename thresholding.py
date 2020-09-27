import cv2

cam = cv2.VideoCapture(0)

x, y, w, h = 270, 190, 100, 100
white = (255, 255, 255)

lower_color = (10, 150, 110)
upper_color = (50, 210, 220)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        raise ValueError('No video')

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame, (x, y), (x+h, y+w), white, thickness=1)
    cv2.putText(frame, "HSV: {0}".format(frame[y+50, x+50]), (x, y+150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, white, thickness=2)

    mask = cv2.inRange(frame, lower_color, upper_color)

    cv2.imshow('Video', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

