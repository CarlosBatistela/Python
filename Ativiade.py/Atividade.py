#1
import random


'''def maior(a, b):
    if a > b:
        print(f"{a} é maior.")
    else:   
        print(f"{b} é maior.")

a=int(input("Digite um número: "))
b=int(input("Digite outro número: "))
maior(a, b)'''

#3
def maior_list(*lista):
    zero = lista[0]
    for i in lista:
        if i > zero:
            zero = i
    print(f"{zero} é o maior número da lista.")

lista = [(random.randint(1,100))  for x in range(10)]
maior_list(*lista)
print(lista)
