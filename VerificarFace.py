import cv2
import face_recognition as fr
import numpy as np
import os
from RegistrarFrequencia import registrar_frequencia

def verificar_rosto(pasta='rostos'):
    cap = cv2.VideoCapture(0)

    quadros_entre_processamento = 5
    contador_quadros = 0


    encodings_salvas = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".npy"):
            encodings_salvas.append(np.load(os.path.join(pasta, arquivo)))

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Erro ao capturar o frame da câmera')
            break

        contador_quadros += 1

        if contador_quadros % quadros_entre_processamento == 0:

            pequena_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_pequena_frame = pequena_frame[:, :, ::-1]


            face_locations = fr.face_locations(rgb_pequena_frame)
            print(f"Localizações de rostos: {face_locations}")

            if len(face_locations) > 0:

                frames_para_comparar = [rgb_pequena_frame.copy() for _ in range(5)]


                rostos_cadastrados = 0
                for frame_comparar in frames_para_comparar:
                    encode_comparar = fr.face_encodings(frame_comparar)

                    if len(encode_comparar) > 0:
                        for encode_teste in encode_comparar:
                            for encode_salvo in encodings_salvas:
                                comparador = fr.compare_faces([encode_salvo], encode_teste)
                                if comparador[0]:
                                    nome = os.path.splitext(arquivo)[0]
                                    registrar_frequencia(nome)
                                    rostos_cadastrados += 1
                                    break

                if rostos_cadastrados == 5:
                    print("Entrada/Saida registrada")
                else:
                    print("Rosto nao encontrado")
                    
        cv2.imshow('Pressione Q para sair', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

verificar_rosto()
