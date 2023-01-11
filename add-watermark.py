import cv2
import numpy

elfs: numpy.ndarray = cv2.imread('images/elfs.jpeg')
watermark: numpy.ndarray = cv2.imread('images/watermark.png')
cv2.imshow('elfs', elfs)
cv2.imshow('watermard', watermark)

print(f'{elfs.shape=}')
print(f'{watermark.shape=}')
x = elfs.shape[1] - watermark.shape[1]
y = elfs.shape[0] - watermark.shape[0]

watermark_place = elfs[y:, x:]
print(watermark_place)
cv2.imshow('watermark_place', watermark_place)

blend = cv2.addWeighted(
                        watermark_place,
                        0.4,
                        watermark,
                        0.6,
                        0
        )
cv2.imshow('blend', blend)

elfs[y:, x:] = blend
cv2.imshow('output', elfs)
cv2.waitKey(0)
