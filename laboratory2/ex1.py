import cv2

# использую камеру ноутбука
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", frameHSV)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cap.release()
cv2.destroyAllWindows()