import random
import string
from datetime import datetime

def menu():
    print("~" * (len("GERADOR DE SENHA") + 4))
    print("  GERADOR DE SENHA  ")
    print("~" * (len("GERADOR DE SENHA") + 4))
    print()
    print("1. Gerar nova senha.")
    print("2. Mostra senhas salvas.")
    print("3. Excluir senhas salvas.")
    print("4. Sair do programa.")
    print()

def user_config():
    while True:
        tamanho_input = input("Quantos caracteres a senha deve conter? ")

        if tamanho_input.isdigit():
            tamanho = int(tamanho_input)
            if tamanho >= 4:
                break
            else:
                print("A senha deve ter pelo menos 4 caracteres.")
        else:
            print("Digite apenas números válidos.")
    while True:
        maiuscula = input("A senha deve conter letras maiusculas? (S/N)").upper() == "S"
        minuscula = input("A senha deve conter letra minuscula? (S/N)").upper() == "S"
        numeros = input("A senha deve conter numeros? (S/N)").upper() == "S"
        caracteres = input("A senha deve conter caracteres? (S/N)").upper() == "S"

        if maiuscula or minuscula or numeros or caracteres:
            break
        else:
            print("\n Você precisa escolher pelo menos uma opção! Tente novamente.\n")

    return tamanho, maiuscula, minuscula, numeros, caracteres


def gerar_senha(tamanho, maiuscula, minuscula, numeros, caracteres):
    caracteres_disponiveis = ""

    if maiuscula:
        caracteres_disponiveis += string.ascii_uppercase
    if minuscula:
        caracteres_disponiveis += string.ascii_lowercase
    if numeros:
        caracteres_disponiveis += string.digits
    if caracteres:
        caracteres_disponiveis += string.punctuation
    if not caracteres_disponiveis:
        print("Você precisa escolher pelo menos um tipo de caractere!")
        return None
    
    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres_disponiveis)

    return senha

def salvar_senha(servico, senha):
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

    with open("senha_salva.txt", "a") as arquivo:
        arquivo.write(f"Serviço: {servico} | Senha: {senha} (Salva em {data_formatada})\n")
    print("Senha salva com sucesso!")


def mostar_senha():
    with open("senha_salva.txt", "r") as arquivo:
        conteudo = arquivo.read()

    if conteudo.strip() == "":
        print("Nenhuma senha foi salva ainda.")
    else:
            print("~" * (len("SENHA SALVAS") + 4))
            print("  SENHA SALVAS  ")
            print("~" * (len("SENHA SALVAS") + 4))
            print()
            print(conteudo)

def excluir_senhas():
    with open("senha_salva.txt", "w") as arquivo:
        arquivo.write("")
    print("Senhas excluídas com sucesso!")


def verificar_servico(servico, senha):
    try:
        with open("senha_salva.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    nova_lista = []
    servico_encontrado = False

    for linha in linhas:
        if linha.startswith(f"Serviço: {servico}"):
            servico_encontrado = True
            opcao = input(f"\n⚠️ O serviço '{servico}' já tem uma senha salva.\nDeseja sobrescrever (S) ou duplicar (D)? ").upper()
            if opcao == "S":
                continue
            elif opcao == "D":
                nova_lista.append(linha)
        else:
            nova_lista.append(linha)


    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nova_linha = f"Serviço: {servico} | Senha: {senha} (Salva em {agora})\n"
    nova_lista.append(nova_linha)

    with open("senha_salva.txt", "w") as arquivo:
        arquivo.writelines(nova_lista)

    if servico_encontrado:
        print("Senha atualizada com sucesso!")
    else:
        print("Senha salva com sucesso!")


while True:
    menu()
    opcao = input("Selecione uma opção: ")

    if opcao == "4":
        print("Encerrando o programa...")
        break

    elif opcao == "1":
        tamanho, maiuscula, minuscula, numeros, caracteres = user_config()
        senha_gerada = gerar_senha(tamanho, maiuscula, minuscula, numeros, caracteres)

        if senha_gerada:
            print(f"\n🔐 Sua senha gerada é: {senha_gerada}")
            while True:
                salvar = input("Você quer salvar essa senha? (S/N) ").upper()
                if salvar == "S":
                    servico = input("Para qual serviço é essa senha? (ex: Instagram, Gmail): ")
                    verificar_servico(servico, senha_gerada)  # Substituir função antiga
                    break
                elif salvar == "N":
                    break
                else:
                    print("Resposta inválida. Digite apenas S ou N.")

    elif opcao == "2":
        mostar_senha()

    elif opcao == "3":
        excluir_senhas()

    else:
        print("⚠️ Selecione uma opção válida!")


