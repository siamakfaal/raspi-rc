import cv2
import time

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #cv2.imshow('Input', frame)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    print(c)
    if c == 27: # Press Esc to exit
        break


cap.release()
cv2.destroyAllWindows()