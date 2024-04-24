import cv2
import os
import numpy as np

def preparar_modelo(path_dataset):
    detector_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    reconhecedor = cv2.face.LBPHFaceRecognizer_create()
    
    faces_conhecidas = []   
    IDs = []
    
    for diretorio, subdirs, arquivos in os.walk(path_dataset):
        for arquivo in arquivos:
            if arquivo.startswitch("."):
                continue
            caminho_img = os.path.join(diretorio, arquivo)
            label = os.path.basename(diretorio)
            imagem = cv2.imread(caminho_img, cv2.IMREAD_GRAYSCALE)
            faces = detector_face.detectMultiScale(imagem, scaleFactor = 1.1, minNeibors = 5)

    for (x, y, w, h) in faces:
        faces_conhecidas.append(imagem[y:y + h, x:x + w])
        IDs.append(int(label))

    reconhecedor.train(faces_conhecidas, np.array(IDs))
    return reconhecedor

def reconhecimento_facial(modelo):
    camera = cv2.VideoCapture(0)

    detector_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    escala_fonte = 1
    cor_fonte = (255, 255, 255)

    while True:
        ret, imagem = camera.read()
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BAYER_BGR2GRAY)
        faces = detector_face.detectMultiScale(imagem_cinza, scaleFactor= 1.1, minNeighbors=5)
        for(x, y, w, h) in faces:
            id_, confianca = modelo.predict(imagem_cinza[y:y + h, x:x + w])
            if confianca <= 100:
                nome = "Pessoa " + str(id_)
            else:
                nome = "Desconhecido"
                cv2.putText(imagem, nome, (x,y + h), fonte, escala_fonte, cor_fonte, 2, cv2.LINE_AA)
                cv2.rectangle(imagem, (x,y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.imshow('Reconhecimento Facial', imagem)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    camera.release()
    cv2.destroyAllWindows()

    #https://hackerculture.com.br/tutorial-reconhecimento-facial-com-opencv/