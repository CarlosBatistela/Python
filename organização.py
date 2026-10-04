import random
aux = 0
lista = []
TmLista = int(input("Quantos números vai ter na lista: "))
for i in range(TmLista):
    lista.append(random.randint(1,100))
    
print(f"Lista{lista}\n")

for p1 in range(len(lista)-1):
    for p2 in range(p1+1, len(lista)):
        if lista[p1] > lista[p2]:
            aux = lista[p1]
            lista[p1] = lista[p2]
            lista[p2] = aux
        print(lista)
        print("----------------")

print(f"\nlista ordenada = {lista} ")

