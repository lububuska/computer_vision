import cv2
import numpy as np

# использую камеру ноутбука
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # нахожу центральный пиксель
    center_x = width // 2
    center_y = height // 2
    
    colors = {
        "red": (0, 0, 255),
        "green": (0, 255, 0),
        "blue": (255, 0, 0)
    }
    
    # bgr центального пикселя
    b, g, r = frame[center_y, center_x]
    
    min_distance = float("inf")
    result = (0, 0, 0)
    for color in colors.values():
        # считаю евклидово расстояние до каждого цвета
        distance = np.sqrt((int(b)-color[0])**2 + (int(g)-color[1])**2 + (int(r)-color[2])**2)
        # ищу ближайший цвет
        if distance < min_distance:
            min_distance = distance
            result = color

    horizontal_width = 200
    horizontal_height = 25
    vertical_width = 25
    vertical_height = 200
    
    horizontal_TLPoint = (center_x - horizontal_width//2, center_y - horizontal_height//2)
    horizontal_BRPoint = (center_x + horizontal_width//2, center_y + horizontal_height//2)
    cv2.rectangle(frame, horizontal_TLPoint, horizontal_BRPoint, result, -1)
    
    top_vertical_TLPoint = (center_x - vertical_width//2, center_y - vertical_height//2)
    top_vertical_BRPoint = (center_x + vertical_width//2, center_y - horizontal_height//2)
    cv2.rectangle(frame, top_vertical_TLPoint, top_vertical_BRPoint, result, -1)
    
    bottom_vertical_TLPoint = (center_x - vertical_width//2, center_y + horizontal_height//2)
    bottom_vertical_BRPoint = (center_x + vertical_width//2, center_y + vertical_height//2)
    cv2.rectangle(frame, bottom_vertical_TLPoint, bottom_vertical_BRPoint, result, -1)
        
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()