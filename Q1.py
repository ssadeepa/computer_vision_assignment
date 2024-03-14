# Reg No: EG/2019/3726
# Question Number 1

import cv2
import numpy as np
import math

def reduceIntensityLevels(image, levels):
    max_val = 255
    factor = max_val / (levels - 1)
    return np.round(image / factor) * factor

# Loading image
image = cv2.imread('./img.jpg')

# Code to reduce intensity levels
while True:
    levels = int(input("Enter the number of intensity levels [2, 4, 8, 16, ...]: "))
    if levels > 0 and math.log2(levels).is_integer():
        break
    else:
        print("Please enter valid number for intensity levels that is an integer power of 2.")

outputIntensityLevels = reduceIntensityLevels(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), levels)

# Display Original Image
cv2.imshow('Original Image', image)
# Display Intensity Levels Image
cv2.imshow('Reduced Intensity Levels Image', outputIntensityLevels)

cv2.waitKey(0)
cv2.destroyAllWindows()