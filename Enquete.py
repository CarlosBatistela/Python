
opcoes = []
votos = []


def cadastrar():
    mais = "s"

    while mais == "s":
        nome = input("Digite a opção: ")
        opcoes.append(nome)
        votos.append(0)
        mais = input("quer cadastrar mais uma? [s/n]: ")

    print("Opções cadastradas!")
    input("\nPressione ENTER para voltar ao menu...")


def listar():
    print("\nOPÇÕES")

    for i in range(len(opcoes)):
        print(i + 1, "-", opcoes[i])

    input("\nPressione ENTER para voltar ao menu...")


def votar():
    print("\nOPÇÕES")

    for i in range(len(opcoes)):
        print(i + 1, "-", opcoes[i])

    continuar =  "s"
    while continuar == "s":
        numero = int(input("escolha: "))

        if numero >= 1 and numero <= len(opcoes):
            votos[numero - 1] = votos[numero - 1] + 1
        else:
            print("Opção inválida!")

        continuar = input("\nvotar de novo? [s/n]: ")

    print("\nVotos registrados!")
    input("\nPressione ENTER para voltar ao menu...")


def consultar():
    print("\nVOTOS")

    for i in range(len(opcoes)):
        print(opcoes[i], "-", votos[i], "votos")

    input("\nPressione ENTER para voltar ao menu...")


def resultado():
    total = 0

    for i in range(len(votos)):
        total = total + votos[i]

    print("\nRESULTADO")

    for i in range(len(opcoes)):
        if total > 0:
            porcentagem = votos[i] * 100 / total
        else:
            porcentagem = 0

        print(opcoes[i], "-", votos[i], "votos -", round(porcentagem, 2), "%")

    input("\nPressione ENTER para voltar ao menu...")


def vencedora():
    maior = 0

    for i in range(len(votos)):
        if votos[i] > maior:
            maior = votos[i]

    print("\nVENCEDORA")

    empate = 0

    for i in range(len(opcoes)):
        if votos[i] == maior:
            print(opcoes[i], "-", votos[i], "votos")
            empate = empate + 1

    if empate > 1:
        print("Houve empate!")

    input("\nPressione ENTER para voltar ao menu...")


while True:

    print("\n===== ENQUETE =====")
    print("1 - Opções")
    print("2 - Lista de opções")
    print("3 - Votação")
    print("4 - Apuração de votos")
    print("5 - Resultado")
    print("6 - Vencedor")
    print("7 - Encerrar")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        cadastrar()

    elif escolha == 2:
        listar()

    elif escolha == 3:
        votar()

    elif escolha == 4:
        consultar()

    elif escolha == 5:
        resultado()

    elif escolha == 6:
        vencedora()

    elif escolha == 7:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")


