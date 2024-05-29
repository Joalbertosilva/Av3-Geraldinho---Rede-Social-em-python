from functions import *

rede = RedeSocial()

while True:
    print("\nO que deseja fazer?")
    print("1. Adicionar usuário")
    print("2. Remover usuário")
    print("3. Adicionar amizade")
    print("4. Remover amizade")
    print("5. Visualizar rede")
    print("6. Buscar usuário")
    print("7. Analisar sentimentos")
    print("8. Calcular centralidade")
    print("9. Identificar comunidades por interesses")
    print("10. Enviar mensagem")
    print("11. Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        interesses = input("Digite os interesses do usuário, separados por vírgula: ").split(",")
        rede.adicionar_usuario(nome, interesses)
    elif opcao == "2":
        nome = input("Digite o nome do usuário a ser removido: ")
        rede.remover_usuario(nome)
    elif opcao == "3":
        usuario1 = input("Digite o nome do primeiro usuário: ")
        usuario2 = input("Digite o nome do segundo usuário: ")
        rede.adicionar_amizade(usuario1, usuario2)
    elif opcao == "4":
        usuario1 = input("Digite o nome do primeiro usuário: ")
        usuario2 = input("Digite o nome do segundo usuário: ")
        rede.remover_amizade(usuario1, usuario2)
    elif opcao == "5":
        rede.visualizar_rede()
    elif opcao == "6":
        nome = input("Digite o nome do usuário a ser buscado: ")
        rede.buscar_usuario(nome)
    elif opcao == "7":
        rede.sentimentos()
    elif opcao == "8":
        rede.centralidade()
    elif opcao == "9":
        rede.comunidades()
    elif opcao == "10":
        usuario1 = input("Digite seu nome: ")
        usuario2 = input("Digite o nome do amigo: ")
        mensagem = input("Digite a mensagem: ")
        rede.enviar_mensagem(usuario1, usuario2, mensagem)
    elif opcao == "11":
        break
    else:
        print("Opção inválida, tente novamente.")