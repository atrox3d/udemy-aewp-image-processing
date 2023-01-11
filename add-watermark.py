import cv2
import numpy

elfs: numpy.ndarray = cv2.imread('images/elfs.jpeg')
watermark: numpy.ndarray = cv2.imread('images/watermark.png')
# cv2.imshow('elfs', elfs)
# cv2.imshow('watermard', watermark)

print(f'{elfs.shape=}')
print(f'{watermark.shape=}')
x = elfs.shape[1] - watermark.shape[1]
y = elfs.shape[0] - watermark.shape[0]
watermark_place = elfs[y:, x:]
print(f'{watermark_place.shape=}')
# cv2.imshow('watermark_place', watermark_place)

alpha = beta = 0.0
# increments = [x/10 for x in range(10)]
# decrements = [x/10 for x in range(10, 0, -1)]
# for alpha, beta in zip(decrements, decrements):
while True:
    print(f'{alpha=}, {beta=}')
    blend = cv2.addWeighted(
                            watermark_place,
                            alpha,
                            watermark,
                            beta,
                            0
            )
    # cv2.imshow('blend', blend)
    elfs[y:, x:] = blend
    cv2.imshow('output', elfs)

    key = cv2.waitKey(0)
    print(f'{key=}')
    match key:
        case 113:
            break
        case 119:
            alpha = round(alpha + 0.1, 1)
        case 115:
            alpha = round(alpha - 0.1, 1)
        case 100:
            beta = round(beta + 0.1, 1)
        case 97:
            beta = round(beta - 0.1, 1)
        case 32:
            alpha = beta = 0.5

    cv2.destroyAllWindows()
