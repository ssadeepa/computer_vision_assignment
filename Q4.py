# Reg No: EG/2019/3726
# Question Number 4

import cv2
import numpy as np

def reduce_resolution(img, block_size):
    rows, cols = img.shape[:2]
    for row in range(0, rows, block_size):
        for col in range(0, cols, block_size):
            block = img[row:row+block_size, col:col+block_size]
            avg = np.mean(block)
            img[row:row+block_size, col:col+block_size] = avg
    return img

# Loading image
image = cv2.imread('img.jpg')

# Reduce resolution with different block sizes.
output_image_3x3_block = reduce_resolution(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).copy(), 3)
output_image_5x5_block = reduce_resolution(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).copy(), 5)
output_image_7x7_block = reduce_resolution(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).copy(), 7)

# Display Original Image
cv2.imshow('Original Image', image)

# Display Block Avg Filter
cv2.imshow('3x3 Block Average', output_image_3x3_block)
cv2.imshow('5x5 Block Average', output_image_5x5_block)
cv2.imshow('7x7 Block Average', output_image_7x7_block)

cv2.waitKey(0)
cv2.destroyAllWindows()



