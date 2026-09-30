


def soma(n1,n2):
    r= n1 + n2
print(F"{n1} + {n2} = {r}")

def subtração(n1,n2):
    r= n1 - n2
print(F"{n1} - {n2} = {r}")

def multiplicação(n1,n2):
    r= n1 * n2
print(F"{n1} X {n2} = {r}")

def divisão(n1,n2):
    r= n1 / n2
print(F"{n1} / {n2} = {r}")

def porcentegem(n1,n2):
    r= (n1 * n2) / 100
print(F"{n2}% de {n1} = {r}")

n1 = float(input("Número: "))
print("oções: +")
print("oções: -")
print("oções: x")
print("oções: /")
print("oções: %")
print("obs: caso esolha %, n2 = a porcetagem)")
operacao = input("operação: ")
n2 = float(input("Número: "))

match operacao:
    case +
soma()

case -
subtração()

case X
multiplicação()

case /







