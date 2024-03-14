# Reg No: EG/2019/3726
# Question Number 3

import cv2

def rotateImage(img, angle):
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(img, M, (cols, rows))

# Loading image
image = cv2.imread('img.jpg')

# Rotate image by 45 & 90 degrees
rotated_45 = rotateImage(image, 45)
rotated_90 = rotateImage(image, 90)

# Display Original Image
cv2.imshow('Original Image', image)

# Display Rotated Image
cv2.imshow('Rotated by 45 Degrees', rotated_45)
cv2.imshow('Rotated by 90 Degrees', rotated_90)

cv2.waitKey(0)
cv2.destroyAllWindows()
