import cv2
import numpy as np

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
x_, y_ = 0, 0
r = 15  # circle radius


# mouse callback function
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode, x_, y_, r

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        x_, y_ = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        copy = img.copy()
        x_, y_ = x, y
        if mode:
            cv2.rectangle(copy, (ix, iy), (x_, y_), (0, 255, 0), 1)
            cv2.imshow("image", copy)
        else:
            cv2.circle(copy, (x, y), r, (0, 0, 255), 1)
            cv2.imshow('image', copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        else:
            cv2.circle(img, (x, y), r, (0, 0, 255), 1)


img = np.zeros((512,512,3), np.uint8)
temp_img = np.copy(img)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_shape)

while True:
    cv2.imshow('image',img)

    if not cv2.EVENT_MOUSEMOVE:
        copy = img.copy()

        if mode:
            cv2.rectangle(copy, (ix, iy), (x_, y_), (0, 255, 0), 1)
            cv2.imshow('image', copy)
        else:
            cv2.circle(copy, (x_, y_), r, (0, 0, 255), 1)
            cv2.imshow('image',copy)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('m'):
        mode = not mode
        x_, y_ = -10, -10
        ix, iy = -10, -10

    elif k == ord('r') and not mode:  # make circle bigger
        r += 1

    elif k == ord('t') and not mode:  # make circle smaller
        if r <= 2:
            r = 1
        else:
            r -= 1

    elif k == ord('x'):  # resets the image (removes circles and rectangles)
        img = np.copy(temp_img)
        x_, y_ = -10, -10
        ix, iy = -10, -10

    elif k == 27:
        break

cv2.destroyAllWindows()
