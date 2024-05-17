from CadastrarFace import CadastrarFace as CF
from VerificarFace import VerificarFace as VF

class Menu:
    
    def Menu():
        while True:
            print('1. Cadastrar\n2. Verificar')
            escolha = input('Escolha uma opção: ')
            if escolha == '1':
                nome = input('Digite o nome')
                CF.cadastrar_face(nome)
                print(f'Cadastrado{nome.upper}')
                break
            elif escolha == '2':
                VF.verificar_face()
                break
            else:
                print('1. Cadastrar\n2. Verificar')
                escolha = input('Escolha uma opção válida')