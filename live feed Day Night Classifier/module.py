import cv2
import numpy as np
import pandas

def hsvSum(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)/255.
    valSum = np.sum(img[:,:,2])
    return valSum

def CameraHSVsum(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)/255.
    valSum = np.sum(img[:,:,2])
    return valSum