import numpy as np
import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()

i = 0

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if i % 2 == 0:
        gaze.refresh(frame)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = ""

    if gaze.pupils_located:
        text = "TAKJESTXDDD"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)


    # Display the resulting frame

    if cv2.waitKey(1) == ord('q'):
        break
    i += 1

    frame = gaze.annotated_frame()

    cv2.imshow('EyeTrack', frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
