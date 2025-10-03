import cv2

# беру картинки трех разных разрешений
# и для каждой картинки устанавливаю разные флаги для чтения
image1 = cv2.imread("img1.png", cv2.IMREAD_REDUCED_COLOR_8)
image2 = cv2.imread("img2.jpg", cv2.IMREAD_UNCHANGED)
image3 = cv2.imread("img3.webp", cv2.IMREAD_GRAYSCALE)

# для каждого окна разные флаги создания окна
cv2.namedWindow("Image 1", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Image 1", image1)

cv2.namedWindow("Image 2", cv2.WINDOW_NORMAL)
cv2.imshow("Image 2", image2)

cv2.namedWindow("Image 3", cv2.WINDOW_FULLSCREEN)
cv2.imshow("Image 3", image3)

cv2.waitKey(0) #завершение программы по нажатию на кнопку
cv2.destroyAllWindows() #закрытие всез окон, используемых в программе