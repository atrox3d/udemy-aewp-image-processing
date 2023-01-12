import cv2
import numpy
from pathlib import Path

import image_helpers

columns = 3
rows = 2

hmargin = 40
vmargin = 20

image_paths = [file.__str__() for file in Path('collage-images/').glob('*')]
images = []
for path in image_paths:
    image = cv2.imread(path)
    height, width, depth = image.shape
    # print(f'{path=}, {image.shape=}')
    image_dict = dict(path=path, image=image, height=height, width=width, depth=depth)
    images.append(image_dict)


max_height = max(item['height'] for item in images)
max_width = max(item['width'] for item in images)
max_depth = max(item['depth'] for item in images)

big_image = numpy.zeros(
                    (
                        max_height * rows + hmargin * (rows + 1),
                        max_width * columns + vmargin * (columns + 1),
                        max_depth
                    ),
                    numpy.uint8
            )

big_image.fill(255)
big_image[:] = [255, 255, 255]

positions = [(x, y) for x in range(columns) for y in range(rows)]

for (pos_x, pos_y), image_dict in zip(positions, images):
    path = image_dict['path']
    width = image_dict['width']
    height = image_dict['height']
    image = image_dict['image']

    x = pos_x * (width + vmargin) + vmargin
    y = pos_y * (height + hmargin) + hmargin

    big_image[y:y+height, x:x+width] = image


small_image = image_helpers.resize(big_image, width=800, height=600)
cv2.imshow('', small_image)
cv2.waitKey(0)
