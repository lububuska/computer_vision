import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_red1 = np.array([0, 150, 120])
upper_red1 = np.array([8, 255, 255])
lower_red2 = np.array([170, 150, 120])
upper_red2 = np.array([180, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask1 = cv2.inRange(frameHSV, lower_red1, upper_red1)
    mask2 = cv2.inRange(frameHSV, lower_red2, upper_red2)
    mask_union = cv2.bitwise_or(mask1, mask2)
    
    #kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) так не очень хорошо, оказывается надо, чтобы типа был именно uint8, чтобы openCV не ругался
    
    # определяю ядро, выбрала матрицу три на три, состящую из единиц
    kernel = np.ones((3,3), np.uint8)
    
    # просто решила посмотреть, как выглядит эрозия (нужна, чтобы шумов не было)
    eroded_mask = cv2.erode(mask_union, kernel)
    
    # также решила посмотреть, как выглядит дилатация (нужна, чтобы дырки убрать)
    dilated_mask = cv2.dilate(mask_union, kernel)
    
    # применяю открытие, снала убираю шумы, потом восстанавливаю контур
    opened_mask = cv2.morphologyEx(mask_union, cv2.MORPH_OPEN, kernel)
    
    # применяю закрытие, снала убираю дырки и расширую форму, потом восстанавливаю контур до исходного
    closed_mask = cv2.morphologyEx(mask_union, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow("Erosion", eroded_mask)
    
    cv2.imshow("Dilatation", dilated_mask)
    
    cv2.imshow("Opening", opened_mask)
    
    cv2.imshow("Closing", closed_mask)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cap.release()
cv2.destroyAllWindows()