import os
import datetime

def registrar_frequencia(nome, pasta='frequencia'):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    # Cria uma subpasta com o nome da pessoa
    subpasta = os.path.join(pasta, nome)
    if not os.path.exists(subpasta):
        os.makedirs(subpasta)
    
    # Define o nome do arquivo com a data atual
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
    arquivo = os.path.join(subpasta, f"{data_atual}.txt")
    
    # Obtém o horário atual
    horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(arquivo):
        with open(arquivo, 'r+') as f:
            linhas = f.readlines()
            if len(linhas) == 0:
                f.write(f"Entrada: {horario}\n")
            else:
                # Atualiza a "Saída"
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