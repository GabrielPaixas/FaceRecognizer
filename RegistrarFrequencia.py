import datetime
import os

def registrar_frequencia(nome, pasta='frequencia'):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    arquivo = os.path.join(pasta, f"{nome}.txt")

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