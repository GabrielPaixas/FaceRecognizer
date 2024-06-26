from CadastrarFace import cadastrar_rosto
from VerificarFace import verificar_rosto

while True:
    escolha = input("1. Cadastrar\n2. Verificar\n3. Sair\n")

    if escolha == "1":
        nome = input("Nome: ")
        cadastrar_rosto(nome)
    elif escolha == "2":
        verificar_rosto()
    else:
        break
        