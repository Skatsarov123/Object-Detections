

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([36, 0, 0])
    upper_green = np.array([70, 255, 255])

    lower_brown = np.array([6, 0, 0])
    upper_brown = np.array([15, 255, 255])
    
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_brown, upper_brown)

    mask = cv2.bitwise_or(mask1, mask2)
    mask4 = cv2.bitwise_or(mask, mask3)
    result = cv2.bitwise_and(frame, frame, mask=mask4)
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()