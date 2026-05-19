import numpy as np
import cv2
from mss import mss

boundingBox = {'top': 90, 'left': 810, 'width': 950, 'height': 20}

geen = [44, 205, 175, 255]

MSS = mss()

while True:
    screenshot = MSS.grab(boundingBox)
    cv2.imshow('capture', np.array(screenshot))

    colourLine = screenshot.pixels[10]

    cv2.waitKey(1)