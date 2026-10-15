n1 = float(input("Número: "))
print("\n--------------------------------------")
print("opções: +")
print("opções: -")
print("opções: x")
print("opções: /")
print("opções: %")
print("(obs: caso esolha %, n2 = porcetagem)")
operacao = input("operação: ")
print("--------------------------------------")
n2 = float(input("\nNúmero: "))
r = 0

def soma():
    r= n1 + n2
    print(F"\n{n1} + {n2} = {r}")

def subtração():
    r= n1 - n2
    print(F"\n{n1} - {n2} = {r}")

def multiplicação():
    r= n1 * n2
    print(F"\n{n1} X {n2} = {r}")

def divisão():
    r= n1 / n2
    print(F"\n{n1} / {n2} = {r}")

def porcentegem():
    r= (n1 * n2) / 100
    print(F"\n{n2}% de {n1} = {r}")


match operacao:
    case "+":
        soma()

    case "-":       
        subtração()

    case "x":
        multiplicação()

    case "/":
        divisão()

    case "%":
        porcentegem()






