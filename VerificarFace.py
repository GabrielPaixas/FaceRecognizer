import cv2
import os
import face_recognition as fr 
import numpy as np

class VerificarFace:
    
    def verificar_face():
        pasta= r'faces'
        cap = cv2.VideoCapture(0)
        
        cadastros = {}
        for cadastro in  os.listdir(pasta):
            if cadastro.endswith(".npy"):
                nome = os.path.splitext(cadastro)[0]
                encode_salvo = np.load(os.path.join(pasta, cadastro))
                cadastros[nome] = encode_salvo
        
        while True:
            ret, frame = cap.read()
            if not ret:
               break
            
            cv2.imshow('Pressione Q para fazer a captura', frame)
            
            if cv2.waitKey(1) & 0xFF == ord ('q'):
                encode_test = fr.face_encodings(frame)
                if len(encode_test) > 0:
                    comparador = fr.compare_faces(encode_salvo, encode_test)
                    if comparador[0]:
                        print(f'Reconhecido: {nome}\n')
                        break
                        
                else:
                    print('Não cadastrado')
                    break
                    
        cap.release()
        cv2.destroyAllWindows()
        