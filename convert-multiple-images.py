from pathlib import Path
import cv2

color_dir = Path('images/')
gray_dir = Path('gray-images/')

color_images = color_dir.glob('*.jpeg')

for color_path in color_images:
    print(color_path)
    color = cv2.imread(str(color_path), 0)
    gray_path = gray_dir / color_path.name
    print(gray_path)
    cv2.imwrite(str(gray_path), color)

