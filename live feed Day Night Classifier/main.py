import cv2
import numpy as np
from config import videoPath
from module import CameraHSVsum
import imutils

v = []
font = cv2.FONT_HERSHEY_SIMPLEX
coord = (180, 270)
fontScale = 1
textColor = (34,242,56)
thickness = 2

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def cameraInput():
    cap = cv2.VideoCapture(videoPath)
    while cap.isOpened():
        ret, frame = cap.read()
        # frame = rescale_frame(frame, percent=50)
        # frame = imutils.resize(frame, width=600)
        valueSum = CameraHSVsum(frame)
        v.append(valueSum)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.putText(frame, str(("day" if valueSum >= 178425.10588235295 else "night", frame.shape)), coord, font, fontScale, textColor, thickness, cv2.LINE_AA)
        cv2.imshow("Window", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if "__main__":
    cameraInput()

#Hw: do a project on color classification (3 colors) (4 images for each color) Don't forget to convert from bgr to hsv but use the saturation channel
    #have an initial analasys of the images like we did before in jupyter notebook
    # also create a test image (download) and test its average
    #revise concepts on pandas
    # put this project and the day night classifier in github