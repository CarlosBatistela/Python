import random
aux = 0
lista = []
ordlista = []
for i in range(5):
    lista.append(random.randint(1,100))
    
print(lista)
print("----------------")

for p1 in range(len(lista)-1):
    for p2 in range(p1+1, len(lista)):
        if lista[p1] > lista[p2]:
            aux = lista[p1]
            lista[p1] = lista[p2]
            lista[p2] = aux
        print(lista)
        print("----------------")
for p1 in range(len(lista)):
    ordlista.append(lista[p1])

print(f"\n     lista     = {lista}\nlista ordenada = {ordlista} ")

