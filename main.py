import numpy as np
import cv2
import keyboard
from mss import mss

boundingBox = {'top': 90, 'left': 810, 'width': 950, 'height': 20}

geen = [44, 205, 175]
yellow = [254, 247, 166]
black = [0, 0, 0]

MSS = mss()

while True:
    screenshot = MSS.grab(boundingBox)

    colourLine = screenshot.pixels[10]

    firstGreenIndex = -1
    lastGreenIndex = -1

    currentYellowIndex = -1

    for pixel in colourLine:
        currentPixelIndex = colourLine.index(pixel)

        if (all(map(lambda x, y: (x - y) / 255 <= 0.1, pixel, geen))):
            if (firstGreenIndex == -1):
                firstGreenIndex = currentPixelIndex
            lastGreenIndex = currentPixelIndex

            pixel = geen
            break
                

        if (all(map(lambda x, y: (x - y) / 255 <= 0.1, pixel, yellow))):
            currentYellowIndex = currentPixelIndex

            pixel = yellow
            break

        pixel = black

# and all(map(lambda x: x >= 0, [firstGreenIndex, lastGreenIndex, currentYellowIndex]))

    print([firstGreenIndex, lastGreenIndex, currentYellowIndex])

    if (currentYellowIndex < firstGreenIndex):
        #keyboard.press_and_release('d')
        print("d")
    elif (currentYellowIndex > lastGreenIndex):
        #keyboard.press_and_release('a')
        print("a")

    #greenCount = 0
    #yellowCount = 0
    #for pixel in colourLine:
     #   for i in range(0,3):
      #      if ((abs(pixel[i] - geen[i])) / 255 <= 0.1):
       #         greenCount += 1
#
 #           if ((abs(pixel[i] - yellow[i])) / 255 <= 0.1):
  #              yellowCount += 1
#
 #           if (greenCount == 3):
  #              print("green")
   #             greenCount = 0
#
 #           if (yellowCount == 3):
  #              print("yellow")
   #             greenCount = 0
    #    greenCount = 0
     #   yellowCount = 0

    # screenshot.pixels[10] = colourLine

    print(len(colourLine))
    cv2.imshow('capture', np.asarray(colourLine, dtype=np.float64))

    cv2.waitKey(1)