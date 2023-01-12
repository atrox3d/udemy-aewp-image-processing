from pathlib import Path

import cv2


def resize(original_image, scale_percentage=None, width=None, height=None):
    """
    resize an image to a % of the original or to specific dimwnsions

    :param scale_percentage: percentage to which scale image
    :param width: width if scale_percentage is None
    :param height: height if scale_percentage is None

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
    """
    resize an image file to a % of the original or to specific dimensions

    :param original_path: path to original image
    :param resized_path: path to resized image, if None expects width and height
    :param scale_percentage: percentage to which scale image
    :param width: width if scale_percentage is None
    :param height: height if scale_percentage is None

    :return: None
    """
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


def get_points_from_rectangle(rectangle):
    """
    extracts 2 point tuples from rectangle
    :param rectangle:
    :return: 2 point tuples
    """
    x1, y1, x2, y2 = rectangle
    pt1 = (x1, y1)
    pt2 = (x2, y2)
    return pt1, pt2
