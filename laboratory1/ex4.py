import cv2

cap = cv2.VideoCapture('video_with_dog.mp4', cv2.CAP_ANY)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# выбираю декодер для видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# создаю файл для записи видео
output_file = cv2.VideoWriter("video_with_dog_output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    
    if not(ret):
        break
    
    cv2.imshow('Video', frame)
    # записываю кадр видео в файл
    output_file.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
output_file.release()
cv2.destroyAllWindows()