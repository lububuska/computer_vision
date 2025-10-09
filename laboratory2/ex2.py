import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# для красного цвета будет два диапазона, от 0 до 10 и от 170 до 180, поэтому hue надо брать из этих двух диапазонов
# saturation помогает отобрать насыщенные оттенки, отличает цвет от серого, больше число - более насыщенный цвет
# value помогает определить цвет светлый или темный, если значение маленькое - цвет темный, например (H=0, S=255, V=100) это темно-красный
# 
# типа стандартный красный

lower_red1 = np.array([0, 100, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 50])
upper_red2 = np.array([180, 255, 255])

# для ярко-красного

# lower_red1 = np.array([0, 150, 120])
# upper_red1 = np.array([8, 255, 255])
# lower_red2 = np.array([170, 150, 120])
# upper_red2 = np.array([180, 255, 255])

# при плохом освещении, тут будет типа красным и оранжевый, и бежевый

# lower_red1 = np.array([0, 60, 40])
# upper_red1 = np.array([15, 255, 220])
# lower_red2 = np.array([165, 60, 40])
# upper_red2 = np.array([180, 255, 220])

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # преобразую кадр из bgr в hsv
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # создаю две маски для диапазонов красного для проверки принадлежности пикселя
    # inRange создает черно-белую маску, если пиксель попадает в диапазон он становится белым, если нет - черным
    mask1 = cv2.inRange(frameHSV, lower_red1, upper_red1)
    mask2 = cv2.inRange(frameHSV, lower_red2, upper_red2)
    mask_union = cv2.bitwise_or(mask1, mask2)

    red_part = cv2.bitwise_and(frame, frame, mask=mask_union)

    # итоговое изображение, где только красное
    cv2.imshow("Red_filter", red_part)
    
    # изображение, где красные пиксели отображаются белыми
    cv2.imshow("Black_and_white_filter", mask_union)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()