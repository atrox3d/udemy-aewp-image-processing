import cv2

color = cv2.imread('images/galaxy.jpeg', 0)
cv2.imwrite('gray-images/galaxy-gray.jpeg', color)


