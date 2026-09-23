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
if media >= 6:
    print("Aprovado")
else :
    print("Reprovado")