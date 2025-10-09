import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# создаю ядро
kernel = np.ones((3,3), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # создаю маски и объединяю их
    mask1 = cv2.inRange(frameHSV, lower_red1, upper_red1)
    mask2 = cv2.inRange(frameHSV, lower_red2, upper_red2)
    mask_union = cv2.bitwise_or(mask1, mask2)
    
    # очищаю маску от шумов
    cleaned_mask = cv2.morphologyEx(mask_union, cv2.MORPH_OPEN, kernel)
    cleaned_mask = cv2.morphologyEx(cleaned_mask, cv2.MORPH_CLOSE, kernel)
    
    # вычисляю контур (массив точек объекта), беру только внешние границы (исключаю возможные дырки) и упрощаю контур
    contours, _ = cv2.findContours(cleaned_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # иду по каждому объекту
    for contour in contours:
        
        # считаю площадь каждого объекта
        area = cv2.contourArea(contour)
        # фильтр мелких объектов
        if area > 500:
            # нахожу координаты прямоугольника (верхний левый угол, ширина и высота)
            x, y, w, h = cv2.boundingRect(contour)
            # рисую черный прямоугольник с толщиной линии 2 на кадре с верхним левым углом в точке (x, y) и правым нижним углом в (x + w, y + h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
            
            # считаю моменты объекта
            M = cv2.moments(contour)
            if M["m00"] != 0:
                # вычисляю центр
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # рисую закрашенный синий круг на кадре с центром в точке (cX, cY), радиусом 3,
                cv2.circle(frame, (cX, cY), 3, (255, 0, 0), -1)
    
    # Отобразить результат
    cv2.imshow("Red Object with Rectangle", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Esc для выхода
        break

cap.release()
cv2.destroyAllWindows()
