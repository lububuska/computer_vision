# Шум соль-перец, должно быть 3 процента белых пикселей и 3 процента черных. 
# Если диагональ изображения имеет хотя бы 1 черный пиксель, то надо главную диагональ покрасить в черный, есть хотя бы 1 белый, но нет черног, то надо покрасить в белый, если черно-белая диагональ - покрасить в черный, если нет ни черного, ни белого - покрасить диагональ в цвет центрального пикселя

import cv2
import random
import numpy as np

image = cv2.imread("img2.png")

h, w, _ = image.shape
num_of_pixels = h * w
num_of_white = int(num_of_pixels * 0.03)
num_of_black = int(num_of_pixels * 0.03)

for _ in range(num_of_white):
    x = random.randint(0, w - 1)
    y = random.randint(0, h - 1)
    image[y, x] = [255, 255, 255]

for _ in range(num_of_black):
    x = random.randint(0, w - 1)
    y = random.randint(0, h - 1)
    image[y, x] = [0, 0, 0]

num_steps = max(h, w)
ys = np.linspace(0, h - 1, num_steps, dtype=int)
xs = np.linspace(0, w - 1, num_steps, dtype=int)

diagonal_pixels = np.array([image[y, x] for x, y in zip(xs, ys)])

flag_white = False
flag_black = False

center_x = w // 2
center_y = h // 2
b, g, r = image[center_y, center_x]

# Проверка диагонали
for pixel in diagonal_pixels:
    if np.all(pixel == [255, 255, 255]):
        flag_white = True
    elif np.all(pixel == [0, 0, 0]):
        flag_black = True

# Выбор цвета
if flag_black:
    color = [0, 0, 0]
elif flag_white and not flag_black:
    color = [255, 255, 255]
else:
    color = [b, g, r]

for x, y in zip(xs, ys):
    image[y, x] = color

cv2.imshow("Task", image)
cv2.waitKey(0)
cv2.destroyAllWindows()