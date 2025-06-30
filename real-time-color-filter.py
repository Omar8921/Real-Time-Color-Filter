import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('Window')

ret, frame = cap.read()
color_filter = None
mask = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if color_filter == 'red':
        lower_bound1 = np.array([0, 100, 100])
        upper_bound1 = np.array([10, 255, 255])

        lower_bound2 = np.array([160, 100, 100])
        upper_bound2 = np.array([179, 255, 255])

        mask1 = cv2.inRange(hsv_frame, lower_bound1, upper_bound1)
        mask2 = cv2.inRange(hsv_frame, lower_bound2, upper_bound2)

        mask = cv2.bitwise_or(mask1, mask2)

    elif color_filter == 'blue':
        lower_bound = np.array([100, 150, 0])
        upper_bound = np.array([130, 255, 255])

        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    elif color_filter == 'green':
        lower_bound = np.array([36, 100, 100])
        upper_bound = np.array([86, 255, 255])

        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    if mask is not None:
        mask = cv2.GaussianBlur(mask, (5,5), 0)

    frame = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Window', frame)
    
    key = cv2.waitKey(1)

    if key in (82, 114):
        color_filter = 'red'
    
    elif key in (66, 98):
        color_filter = 'blue'

    elif key in (71, 103):
        color_filter = 'green'

    elif key in (83, 115):
        cv2.imwrite('screenshot.png', frame)

    elif key == 13:
        mask = None
        color_filter = None

    elif key == 27:
        break


cv2.destroyAllWindows()
cap.release()