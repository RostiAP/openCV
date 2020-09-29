import cv2

cam = cv2.VideoCapture(0)

center = (round(cam.get(3) / 2), round(cam.get(4) / 2))
window_size = 25
x, y = center[0] - round(window_size/2), center[1] - round(window_size/2)
white = (255, 255, 255)

lower_color = (150, 90, 100)
upper_color = (190, 140, 170)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        raise ValueError('No video')

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame, (x, y), (x+window_size, y+window_size), white, thickness=1)
    cv2.putText(frame, "HSV: {0}".format(frame[y+round(window_size/2), x+round(window_size/2)]), (x, y+150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, white, thickness=2)

    mask = cv2.inRange(frame, lower_color, upper_color)

    cv2.imshow('Video', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()