import cv2
import numpy
from pathlib import Path

columns = 3
rows = 2

hmargin = 40
vmargin = 20

image_globs = Path('collage-images/').glob('*')
image_paths = [file.__str__() for file in image_globs]
images = dict()
for path in image_paths:
    image = cv2.imread(path)
    height, width, depth = image.shape
    images.update({path: dict(image=image, height=height, width=width, depth=depth)})

# for name, item in images.items():
#     print(name, item['width'], item['height'])

# for image in images.values():
#     _, height, width = image.values()
#     print(height, width)

max_height = max(item['height'] for name, item in images.items())
max_width = max(item['width'] for name, item in images.items())
max_depth = max(item['depth'] for name, item in images.items())
print(max_height)
print(max_width)
print(max_depth)

big_image = numpy.zeros(
                    (
                        max_height * rows + vmargin * (rows + 1),
                        max_width * columns + hmargin * (columns + 1),
                        max_depth
                    ),
                    numpy.uint8
            )
print(big_image.shape)

big_image.fill(255)
big_image[:] = [255, 255, 255]

positions = [(x, y) for x in range(columns) for y in range(rows)]
print(positions)

l = list(zip(positions, images.items()))
print(l)
# cv2.imshow('', big_image)
# cv2.waitKey(0)
