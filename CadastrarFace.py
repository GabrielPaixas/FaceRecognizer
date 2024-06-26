import cv2
import os
import face_recognition as fr
import numpy as np

def cadastrar_rosto(nome, pasta='rostos'):
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print('erro')
            
        cv2.imshow('Press Q to capture', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            encode = fr.face_encodings(frame)
            if len(encode) > 0:
                encode = encode[0]
                nome_arquivo = os.path.join(pasta, f'{nome}.npy')
                np.save(nome_arquivo, encode)
                break
    cap.release()
    cv2.destroyAllWindows()
