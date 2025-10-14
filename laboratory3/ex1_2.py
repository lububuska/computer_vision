import numpy as np

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
    
# стандартное отклонение
standard_deviation = 2
for size in [3, 5, 7]:
    print(f'Стандартное отклонение {standard_deviation}')
    print(f'Гауссова матрица {size}x{size}:')
    print(make_kernel(size, standard_deviation))
    print()