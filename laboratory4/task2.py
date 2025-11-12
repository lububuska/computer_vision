import numpy as np
import cv2

# формула Гаусса
def gauss(x, y, a, b, sigma):
    return (1 /  (2 * np.pi * sigma * sigma)) * np.exp(-(((x - a) ** 2 + (y - b) ** 2)/(2 * sigma * sigma)))

def make_kernel(kernel_size, standard_deviation):
    kernel = np.zeros((kernel_size, kernel_size), dtype=float)
    a = kernel_size // 2
    b = kernel_size // 2
    sum = 0
    
    for y in range(kernel_size):
        for x in range(kernel_size):
            kernel[y, x] = gauss(x, y, a, b, standard_deviation)
            sum += gauss(x, y, a, b, standard_deviation)
       
    kernel /= np.sum(kernel)
    return kernel, sum

def apply_gaussian_filter_manual(image, kernel):
    height, width = image.shape
    half_kernel = kernel.shape[0] // 2
    result = np.zeros_like(image, dtype=float)

    for y in range(half_kernel, height - half_kernel):
        for x in range(half_kernel, width - half_kernel):
            region = image[y - half_kernel:y + half_kernel + 1, x - half_kernel:x + half_kernel + 1]
            result[y, x] = np.sum(region * kernel)
    
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

def task1(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    resized_img = cv2.resize(img, (480, 360), interpolation=cv2.INTER_AREA)
    
    standard_deviation = 1
    size = 3

    matrix, summa = make_kernel(size, standard_deviation)

    blurred = apply_gaussian_filter_manual(resized_img, matrix)
    
    return blurred
    
def task2(image):
    # матрицы в операторе Собеля
    G_x_kernel = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]], dtype = float)
    G_y_kernel = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]], dtype = float)
    
    height, width = image.shape
    # создаю матрицы из нулей, которые будут использоваться для свертки
    G_x = np.zeros((height, width), dtype = float)
    G_y = np.zeros((height, width), dtype = float)
    
    # прохожу по нулевым матрицам и заменяю пиксель значение суммы произведения пиксля на матрицу собеля, т.е. нахожу производную
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            region = image[i - 1:i + 2, j - 1:j + 2]
            G_x[i, j] = np.sum(region * G_x_kernel)
            G_y[i, j] = np.sum(region * G_y_kernel)
    
    # нахожу матрицу значений длин и матрицу значений углов
    length = np.sqrt(G_x ** 2 + G_y ** 2)
    angle = np.arctan2(G_y, G_x) * (180.0 / np.pi)
    
    # нормирую чтобы нормальная картинка была
    length_display = cv2.normalize(length, None, 0, 255, cv2.NORM_MINMAX)
    angle_display = (angle + 180) * (255.0 / 360.0)
    
    cv2.imshow("Nornalized length", np.uint8(length_display))
    cv2.imshow("Normalized angle", np.uint8(angle_display))
    
    print(length_display)
    print(angle_display)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
blurred_image = task1("/Users/mariamasenko/University/7_semestr/cv/laboratory4/cat_img.jpg")
task2(blurred_image)
