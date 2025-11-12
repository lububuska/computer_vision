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
    
    cv2.imshow("Original", resized_img)
    cv2.imshow(f"Gaussian Filter {size}x{size}", blurred)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
task1("/Users/mariamasenko/University/7_semestr/cv/laboratory4/cat_img.jpg")