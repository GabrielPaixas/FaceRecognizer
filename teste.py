import cv2
import face_recognition as fr 
import os
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
    
def verificar_rosto(pasta='rostos'):
    cap = cv2.VideoCapture(0)
    
    # Dicionário para armazenar os rostos cadastrados
    rostos_cadastrados = {}
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".npy"):
            nome_rosto = os.path.splitext(arquivo)[0]  # Remover a extensão .npy para obter o nome do rosto
            encode_salvo = np.load(os.path.join(pasta, arquivo))
            rostos_cadastrados[nome_rosto] = encode_salvo
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print('erro')
            break
        
        cv2.imshow('Pres Q to capture', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            encode_teste = fr.face_encodings(frame)
            if len(encode_teste) > 0:
                encode_teste = encode_teste[0]
                for nome, encode_salvo in rostos_cadastrados.items():
                    comparador = fr.compare_faces([encode_salvo], encode_teste)
                    if comparador[0]:
                        print("Rosto cadastrado:", nome)
                        break
                else:
                    print("Rosto não cadastrado")
                    break
                
    cap.release()
    cv2.destroyAllWindows()
        
    
escolha = input("\n1. Cadastrar\n2. Verificar\n")

if escolha == "1":
    nome = input("Nome: ")
    cadastrar_rosto(nome)
elif escolha == "2":
    verificar_rosto()
