import cv2
from pathlib import Path


def calculate_size(scale_percentage, width, height):
    w = width * scale_percentage / 100
    h = height * scale_percentage / 100
    return int(h), int(w)


def resize(image_path, scale_percentage, resized_path=None):
    image = cv2.imread(image_path)

    print(f'{image.shape=}')
    height, width, _ = image.shape

    h, w = calculate_size(scale_percentage, width, height)
    dsize = w, h
    print(f'{dsize=}')

    resized = cv2.resize(image, dsize)
    print(f'{resized.shape=}')

    if not resized_path:
        path = Path(image_path)
        height, width, _ = resized.shape
        dims = f'{height}x{width}'
        filename = f'{path.stem}-{dims}{path.suffix}'
        resized_path = Path('resized-images', filename).__str__()

    print(resized_path)
    cv2.imwrite(resized_path, resized)


resize('images/galaxy.jpeg', 20)

