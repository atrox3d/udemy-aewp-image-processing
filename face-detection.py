import cv2
import numpy
from pathlib import Path


def resize(original_image, scale_percentage=None, width=None, height=None):
    """
    resize an image to a % of the original
    :param height:
    :param width:
    :param original_image:
    :param scale_percentage:
    :return: resized image
    """
    print(f'{original_image.shape=}')
    original_height, original_width, _ = original_image.shape

    if scale_percentage:
        w = int(original_width * scale_percentage / 100)
        h = int(original_height * scale_percentage / 100)
    elif width and height:
        w = width
        h = height
    else:
        raise ValueError('Either scale_percentage or width and height must be valorized!')

    # invert width and height
    dsize = w, h
    print(f'{dsize=}')

    resized_image = cv2.resize(original_image, dsize)
    print(f'{resized_image.shape=}')

    return resized_image


def resize_imagefile(original_path, resized_path=None, scale_percentage=None, width=None, height=None):
    original_image = cv2.imread(original_path)
    resized_image = resize(original_image, scale_percentage, width, height)

    if not resized_path:
        path = Path(original_path)
        height, width, _ = original_image.shape
        name = path.stem
        ext = path.suffix
        filename = f'{name}-{width}x{height}{ext}'
        resized_path = path.with_name(filename).__str__()
    cv2.imwrite(resized_path, resized_image)


if __name__ == '__main__':
    original_image: numpy.ndarray = cv2.imread('images/humans.jpeg')
    print(f'{original_image.shape=}')

    resized_image: numpy.ndarray = resize(original_image, 50)
    print(f'{resized_image.shape=}')

    target_image = resized_image.copy()
    face_cascade = cv2.CascadeClassifier('faces.xml')
    faces = face_cascade.detectMultiScale(target_image, 1.1, 4)
    print(f'{faces=}')

    rectangles = [[x, y, x+w, y+h] for x, y, w, h in faces]
    print(f'{rectangles=}')

    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        pt1 = (x1, y1)
        pt2 = (x2, y2)
        color = (255, 255, 255)
        cv2.rectangle(target_image, pt1, pt2, color, 3)

    cv2.imshow('image', resized_image)
    cv2.imshow('faces', target_image)
    key = cv2.waitKey(0)
    print(key)