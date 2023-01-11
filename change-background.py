import cv2
import numpy

foreground: numpy.ndarray = cv2.imread('images/giraffe.jpeg')
background: numpy.ndarray = cv2.imread('images/safari.jpeg')

green_pixel = foreground[0, 0]
print(f'{green_pixel=}')

height, width, _ = foreground.shape
print(f'{width=}, {height=}')

resized_background = cv2.resize(background, (width, height))

count = 0
for x in range(width):
    for y in range(height):
        pixel = foreground[y, x]
        if numpy.any(pixel == [0, 255, 0]):
        # if pixel[1] > 250:
            count += 1
            print(f'found: {count:,}')
            foreground[y, x] = resized_background[y, x]

cv2.imshow('merge', foreground)
cv2.waitKey(0)
