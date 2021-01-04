import numpy as np
import cv2
import time
from gaze_tracking import GazeTracking

cap = cv2.VideoCapture(0)


MAX_FPS = cap.get(cv2.CAP_PROP_FPS)

fps = 10

passed = float(0)
prev = time.time()

gaze = GazeTracking()

while(True):
    if passed >= (1 / fps):

        # Capture frame-by-frame
        ret, frame = cap.read()
        gaze.refresh(frame)

        if gaze.pupils_located:
            text = "Eyes found"
        else:
            text = "Eyes 404"

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        cv2.putText(frame, gaze.direction(), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        frame = gaze.annotated_frame()


        # Display the resulting frame
        cv2.imshow('Demo', frame)
        if cv2.waitKey(1) == ord('q'):
            break

        prev = t
    t = time.time()
    passed = t - prev
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()