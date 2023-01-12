import cv2
import numpy
from pathlib import Path

import image_helpers

if __name__ == '__main__':
    rootdir = Path('face-detection-images/')
    for image_path in rootdir.glob('*'):
        original_image: numpy.ndarray = cv2.imread(image_path.__str__())
        if original_image is None:
            continue
        print(f'{original_image.shape=}')

        resized_image: numpy.ndarray = image_helpers.resize(original_image, 60)
        print(f'{resized_image.shape=}')

        base_image = resized_image
        target_image = resized_image.copy()
        face_cascade = cv2.CascadeClassifier('faces.xml')
        faces = face_cascade.detectMultiScale(target_image, 1.1, 4)
        print(f'{faces=}')

        rectangles = [[x, y, x+w, y+h] for x, y, w, h in faces]
        print(f'{rectangles=}')

        for rectangle in rectangles:
            pt1, pt2 = image_helpers.get_points_from_rectangle(rectangle)
            color = (0, 255, 0)
            cv2.rectangle(target_image, pt1, pt2, color, 3)

        cv2.imshow('image', base_image)
        cv2.imshow('faces', target_image)

        key = cv2.waitKey(0)
        print(key)
        if key == 113:
            break
