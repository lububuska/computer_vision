import cv2

image1 = cv2.imread("img1.jpg") #загружаю картинку в программу
cv2.namedWindow("Task 1") #создаю окно для отображения картинки
cv2.imshow("Task 1", image1) # размещаю картинку в окне
cv2.waitKey(0) #завершение программы по нажатию на кнопку
cv2.destroyAllWindows() #закрытие всез окон, используемых в программе