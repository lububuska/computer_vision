import numpy as np
import cv2

# формула Гаусса
def gauss(x, y, a, b, sigma):
    return (1 /  (2 * np.pi * sigma * sigma)) * np.exp(-(((x - a) ** 2 + (y - b) ** 2)/(2 * sigma * sigma)))

# строю матрицу Гаусса по переданному размеру ядра и стандартному отклонению
def make_kernel(kernel_size, standard_deviation):
    kernel = np.zeros((kernel_size, kernel_size), dtype=float)
    a = kernel_size // 2
    b = kernel_size // 2
    
    for y in range(kernel_size):
        for x in range(kernel_size):
            kernel[y, x] = gauss(x, y, a, b, standard_deviation)
     
    # нормирую матрицу, чтобы сумма элементов равнялась 1     
    kernel /= np.sum(kernel)
    return kernel

# применяю 
def apply_gaussian_filter_manual(image, kernel):
    height, width = image.shape
    half_kernel = kernel.shape[0] // 2
    # пустое изображение для записи результата
    result = np.zeros_like(image, dtype=float)

    # иду по каждому пикселю кроме крайних
    for y in range(half_kernel, height - half_kernel):
        for x in range(half_kernel, width - half_kernel):
            # вырезаю как бы область вокруг центрального пикселя по размеру ядра
            region = image[y - half_kernel:y + half_kernel + 1, x - half_kernel:x + half_kernel + 1]
            # умножаю каждый пиксель из region на соответствующее значение из ядра и суммирую все (это свертка,значение центрального пикселя)
            result[y, x] = np.sum(region * kernel)
    
    # ограничиваю значения цвета от 0 до 255
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)
    
img = cv2.imread("skebob.jpg", cv2.IMREAD_GRAYSCALE)
resized_img = cv2.resize(img, (480, 360), interpolation=cv2.INTER_AREA)


# стандартное отклонение, чем оно больше, тем больше размытие (типа соседние пиксели сильнее влияют)
standard_deviation = 20
for size in [3, 5, 7]:
    print(f'Стандартное отклонение {standard_deviation}')
    print(f'Гауссова матрица {size}x{size}:')
    print(make_kernel(size, standard_deviation))
    blurred = apply_gaussian_filter_manual(resized_img, make_kernel(size, standard_deviation))
    cv2.imshow(f"Gaussian Filter {size}x{size}", blurred)
    print()
    
cv2.imshow("Original", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()