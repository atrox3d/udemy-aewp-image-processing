import cv2


def calculate_size(scale_percentage, width, height):
    w = width * scale_percentage / 100
    h = height * scale_percentage / 100
    return int(w), int(h)


def resize(image_path, scale_percentage, resized_path):
    image = cv2.imread(image_path)
    print(f'{image.shape=}')
    height, width, _ = image.shape
    dsize = calculate_size(scale_percentage, width, height)
    print(f'{dsize=}')
    resized = cv2.resize(image, dsize)
    print(f'{resized.shape=}')
    cv2.imwrite(resized_path, resized)


resize('images/galaxy.jpeg', 20, 'images/galaxy-resized.jpg')

