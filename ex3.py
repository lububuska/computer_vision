import cv2

# открываю видеофайл и возвращаю объект для покадрового чтения
cap = cv2.VideoCapture('video_with_dog.mp4', cv2.CAP_ANY)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(width, height)

while True:
    # записываю кадр видео в frame в виде двумерной матрицы, использую флаг ret для результата чтения
    ret, frame = cap.read()
    
    if not(ret):
        break
    
    frame = cv2.resize(frame, (int(width//2), int(height//2))) # изменила размер кадров
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #изменила цвет кадров
    
    # отображаю кадр в окне
    cv2.imshow('Video', gray)
    # жду одну милисекунду, проверяю нажата ли клавиша esc, если да, завершаю цикл, если нет, читаю следующий кадр
    if cv2.waitKey(1) & 0xFF == 27:
        break