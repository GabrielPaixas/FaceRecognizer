import face_recognition as fr
import numpy as np
import cv2

def classificar_rosto(encode_teste, encodings_salvas, nomes_encodings, frame, face_location):
    comparacoes = fr.compare_faces(encodings_salvas, encode_teste)
    distancias = fr.face_distance(encodings_salvas, encode_teste)
    melhor_ajuste_index = np.argmin(distancias)
    
    if comparacoes[melhor_ajuste_index]:
        nome = nomes_encodings[melhor_ajuste_index]
    else:
        nome = "Desconhecido"

    top, right, bottom, left = face_location
    top *= 4
    right *= 4
    bottom *= 4
    left *= 4

    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    return nome