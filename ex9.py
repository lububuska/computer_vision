import cv2

# считываю видео с камеры телефона через ip webcam
video = cv2.VideoCapture("http://192.168.1.51:8080/video")

while True:
    ret, frame = video.read()
    if not ret:
        break

    cv2.imshow("Camera_phone", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()