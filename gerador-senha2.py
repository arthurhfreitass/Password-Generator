import random
import string
import base64
from datetime import datetime
from colorama import init, Fore, Back, Style
init(autoreset=True)

def menu():
    print(Fore.CYAN + "~" * (len("GERADOR DE SENHA") + 4))
    print(Fore.CYAN + "  GERADOR DE SENHA  ")
    print(Fore.CYAN + "~" * (len("GERADOR DE SENHA") + 4))
    print()
    print(Fore.LIGHTCYAN_EX + Back.BLACK + "1. Gerar nova senha.")
    print(Fore.LIGHTCYAN_EX + Back.BLACK + "2. Mostrar senhas salvas.")
    print(Fore.LIGHTCYAN_EX + Back.BLACK + "3. Excluir senhas salvas.")
    print(Fore.RED + Back.BLACK + "4. Sair do programa.")
    print()

def user_config():
    while True:
        tamanho_input = input(Fore.LIGHTCYAN_EX + "Quantos caracteres a senha deve conter? ")

        if tamanho_input.isdigit():
            tamanho = int(tamanho_input)
            if tamanho >= 4:
                break
            else:
                print(Fore.RED + "A senha deve ter pelo menos 4 caracteres.")
        else:
            print(Fore.RED + "Digite apenas números válidos.")

    while True:
        maiuscula = input(Fore.LIGHTCYAN_EX + "A senha deve conter letras maiusculas? (S/N)").upper() == "S"
        minuscula = input(Fore.LIGHTCYAN_EX + "A senha deve conter letra minuscula? (S/N)").upper() == "S"
        numeros = input(Fore.LIGHTCYAN_EX + "A senha deve conter numeros? (S/N)").upper() == "S"
        caracteres = input(Fore.LIGHTCYAN_EX + "A senha deve conter caracteres? (S/N)").upper() == "S"

        if maiuscula or minuscula or numeros or caracteres:
            break
        else:
            print(Fore.RED + "\n Você precisa escolher pelo menos uma opção! Tente novamente.\n")

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


def mostrar_senha():
    try:
        with open("senha_salva.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhuma senha foi salva ainda.")
        return

    if not linhas:
        print("Nenhuma senha foi salva ainda.")
        return

    print("~" * 30)
    print("   SENHAS SALVAS (modo seguro)  ")
    print("~" * 30)

    lista_formatada = []

    for linha in linhas:
        try:
            parte1, resto = linha.strip().split(" | Senha: ")
            senha_codificada, parte2 = resto.split(" (Salva em ")

            # Decodifica a senha real
            senha_real = base64.b64decode(senha_codificada.encode("utf-8")).decode("utf-8")
            senha_oculta = "*" * len(senha_real)

            nova_linha = f"{parte1} | Senha: {senha_oculta} (Salva em {parte2}"
            print(nova_linha)
            lista_formatada.append((parte1, senha_real, parte2))

        except Exception as e:
            print(f"Erro ao processar linha: {linha.strip()} ({e})")

    print("\nDeseja revelar a senha de algum serviço?")
    opcao = input("(S/N): ").strip().upper()

    if opcao == "S":
        nome_servico = input("Digite o nome do serviço: ").strip().lower()

        encontrado = False
        for servico, senha, data in lista_formatada:
            if nome_servico in servico.lower():
                print(f"\n🔓 {servico} | Senha: {senha} (Salva em {data}")
                encontrado = True
        if not encontrado:
            print("❌ Serviço não encontrado.")




def excluir_senhas():
    with open("senha_salva.txt", "w") as arquivo:
        arquivo.write("")
    print("Senhas excluídas com sucesso!")


def verificar_forca(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_caractere = any(c in string.punctuation for c in senha)

    faltando = []
    if not tem_maiuscula:
        faltando.append("letra maiúscula")
    if not tem_minuscula:
        faltando.append("letra minúscula")
    if not tem_numero:
        faltando.append("número")
    if not tem_caractere:
        faltando.append("caractere especial")

    if not faltando:
        print("💪 Força da senha: Forte ✅")
    else:
        print("⚠️ Força da senha: Fraca ❌")
        print("Motivo: faltando -> " + ", ".join(faltando))


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
            opcao = input(f"\n O serviço '{servico}' já tem uma senha salva.\nDeseja sobrescrever (S) ou duplicar (D)? ").upper()
            if opcao == "S":
                continue
            elif opcao == "D":
                nova_lista.append(linha)
        else:
            nova_lista.append(linha)

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    senha_codificada = base64.b64encode(senha.encode("utf-8")).decode("utf-8")

    nova_linha = f"Serviço: {servico} | Senha: {senha_codificada} (Salva em {agora})\n"
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
            verificar_forca(senha_gerada)
            while True:
                salvar = input("Você quer salvar essa senha? (S/N) ").upper()
                if salvar == "S":
                    servico = input("Para qual serviço é essa senha? (ex: Instagram, Gmail): ")
                    usuario = input("Qual o nome de usuário/login desse serviço? (ex: usuario@gmail.com): ")
                    servico_completo = f"{servico} - {usuario}"
                    verificar_servico(servico_completo, senha_gerada)
                    break
                elif salvar == "N":
                    break
                else:
                    print("Resposta inválida. Digite apenas S ou N.")

    elif opcao == "2":
        mostrar_senha()

    elif opcao == "3":
        excluir_senhas()

    else:
        print("⚠️ Selecione uma opção válida!")


