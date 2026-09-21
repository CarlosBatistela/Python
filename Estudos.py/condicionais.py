nome = input("nome: ")
salario = float(input("salario: "))
Nsalario = 0
dep = int(input("dependentes: "))
match dep:
    case 0:
        Nsalario = salario+(salario*5/100)
        print(Nsalario)
    case 1|2|3:
         Nsalario = salario+(salario*10/100)
         print(f"seu novo sálario é R${Nsalario}")
    case 4|5|6:
        Nsalario = salario+(salario*15/100)
        print(f"seu novo sálario é R${Nsalario}")
    case x if x > 6:
        Nsalario = salario+(salario*10/100)
        print(f"seu novo sálario é R${Nsalario}")

...

aluno = input("Aluno: ")
qtn = int(input("Quantas notas: "))
notas = []
for i in range (qtn):
    nota = float(input("nota: "))
    notas.append(nota)
print(f"notas = {notas}")
media = sum(notas)/qtn
print(F"Média {media}")
match media:
    case i if i > 8.9:
        print("Nota otima")
    case i if i > 7.9:
        print("Nota muito boa")
    case i if i > 6.9:
        print("Nota boa")
    case i if i > 5.9:
        print("Nota razoavel")
    case i if i > 4.9:
        print("Nota ruim")
    case i if 5 > i:
        print("Pessima nota")
if match >= 6:
    print(Aprovado)
else :
    print(Reprovado)