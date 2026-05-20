import numpy as np
import cv2
import keyboard
from PIL import Image
from mss import mss
import time
import mouse

boundingBox = {'top': 90, 'left': 810, 'width': 950, 'height': 20}

geen = (44, 205, 175)
yellow = (254, 247, 166)
red = (255, 0, 0)
black = (0, 0, 0)

MSS = mss()

press = False

spammingF = False

while True:
    screenshot = MSS.grab(boundingBox)

    colourLine = screenshot.pixels[10]

    firstGreenIndex = -1
    lastGreenIndex = -1

    firstYellowIndex = -1

    pixelArray = []

    for pixel in colourLine:
        currentPixelIndex = colourLine.index(pixel)

        colour = black

        if (all(map(lambda x, y: abs((x - y)) / 255 <= 0.1, pixel, geen))):
            if (firstGreenIndex == -1):
                firstGreenIndex = currentPixelIndex
            lastGreenIndex = currentPixelIndex

            colour = geen

        if (all(map(lambda x, y: abs((x - y)) / 255 <= 0.1, pixel, yellow))):
            if (firstYellowIndex == -1):
                firstYellowIndex = currentPixelIndex

            if (pixel == geen):
                colour = red
            else:
                colour = yellow

        pixelArray.append(colour)

    #print(pixelArray)

# and all(map(lambda x: x >= 0, [firstGreenIndex, lastGreenIndex, currentYellowIndex]))

    #print([firstGreenIndex, lastGreenIndex, firstYellowIndex])

    averageGreenIndex = (firstGreenIndex + lastGreenIndex) / 2

    #print(averageGreenIndex)

    if (all(map(lambda x: x >= 0, [firstGreenIndex, lastGreenIndex, firstGreenIndex]))):
        spammingF = False
        if (firstYellowIndex < averageGreenIndex):
            keyboard.release('a')
            keyboard.press('d')
            press = True
            #print("d")
        elif (firstYellowIndex > averageGreenIndex):
            keyboard.release('d')
            keyboard.press('a')
            press = True
            #print("a")
        else:
            #print("TEST")
            press = False
    elif spammingF:
        keyboard.press_and_release('f')
    else:
        time.sleep(3)
        mouse.move(50, 50)
        mouse.click("left")
        spammingF = True


    #print(press)

    if press == False:
        keyboard.release('d')
        keyboard.release('a')

    img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "RGBX")

    img.putdata(pixelArray * 10)

    cv2.imshow('capture', np.array(img))

    cv2.waitKey(1)