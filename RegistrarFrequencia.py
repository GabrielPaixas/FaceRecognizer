import os
import datetime

def registrar_frequencia(nome, pasta='frequencia'):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    subpasta = os.path.join(pasta, nome)
    if not os.path.exists(subpasta):
        os.makedirs(subpasta)
    
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
    arquivo = os.path.join(subpasta, f"{data_atual}.txt")
    
    horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(arquivo):
        with open(arquivo, 'r+') as f:
            linhas = f.readlines()
            if len(linhas) == 0:
                f.write(f"Entrada: {horario}\n")
            else:
                for i, linha in enumerate(linhas):
                    if "Saida" in linha:
                        linhas[i] = f"Saida: {horario}\n"
                        break
                else:
                    linhas.append(f"Saida: {horario}\n")
                f.seek(0)
                f.writelines(linhas)
                f.truncate()
    else:
        with open(arquivo, 'w') as f:
            f.write(f"Entrada: {horario}\n")