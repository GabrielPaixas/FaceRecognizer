import cv2

cap = cv2.VideoCapture(0) # captura de webcam

while(not cv2.waitKey(20) & 0xFF == ord('q')): #mantem a webcam aberta ate a tecla 'q' ser pressionada
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

cap.release() #finaliza a captura

cv2.destroyAllWindows()

cv2.waitKey(1)