import cv2
import os
import face_recognition as fr
import numpy as np

class CadastrarFace:
    def cadastrar_face(nome):
        pasta=r'faces'
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print('Erro')
                
            cv2.imshow('Pressione Q para cadastrar o rosto', frame)
            
            if cv2.waitKey(1) &  0xFF == ord('q'):
                encode = fr.face_encodings(frame)
                if len(encode) > 0:
                    encode = encode[0]
                    nome_arquivo = os.path.join(pasta, f'{nome}.npy')
                    np.save(nome_arquivo, encode)
                    break
        cap.release()
        cv2.destroyAllWindows()