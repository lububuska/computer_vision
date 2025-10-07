import cv2

image = cv2.imread("img1.png") # формат blue green red
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # конвертация в hsv

cv2.namedWindow("Not HSV", cv2.WINDOW_NORMAL)
cv2.imshow("Not HSV", image)

cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
cv2.imshow("HSV", imageHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()