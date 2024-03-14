# Reg No: EG/2019/3726
# Question Number 2

import cv2


def applyAverageFilter(img, kernel_size):
    return cv2.blur(img, (kernel_size, kernel_size))

# Loading image
image = cv2.imread('img.jpg')

# Apply average filter with different kernel sizes
output_image_3x3 = applyAverageFilter(image, 3)
output_image_10x10 = applyAverageFilter(image, 10)
output_image_20x20 = applyAverageFilter(image, 20)

# Display Original Image
cv2.imshow('Original Image', image)

# Average Filter
cv2.imshow('3x3 Average Filter', output_image_3x3)
cv2.imshow('10x10 Average Filter', output_image_10x10)
cv2.imshow('20x20 Average Filter', output_image_20x20)

cv2.waitKey(0)
cv2.destroyAllWindows()
