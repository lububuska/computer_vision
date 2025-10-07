import cv2

# использую камеру ноутбука
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    center_x = width // 2
    center_y = height // 2

    horizontal_width = 200
    horizontal_height = 25
    vertical_width = 25
    vertical_height = 200
    
    horizontal_TLPoint = (center_x - horizontal_width//2, center_y - horizontal_height//2)
    horizontal_BRPoint = (center_x + horizontal_width//2, center_y + horizontal_height//2)
    cv2.rectangle(frame, horizontal_TLPoint, horizontal_BRPoint, (0, 0, 255))
    
    top_vertical_TLPoint = (center_x - vertical_width//2, center_y - vertical_height//2)
    top_vertical_BRPoint = (center_x + vertical_width//2, center_y - horizontal_height//2)
    cv2.rectangle(frame, top_vertical_TLPoint, top_vertical_BRPoint, (0, 0, 255))
    
    bottom_vertical_TLPoint = (center_x - vertical_width//2, center_y + horizontal_height//2)
    bottom_vertical_BRPoint = (center_x + vertical_width//2, center_y + vertical_height//2)
    cv2.rectangle(frame, bottom_vertical_TLPoint, bottom_vertical_BRPoint, (0, 0, 255))
        
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()