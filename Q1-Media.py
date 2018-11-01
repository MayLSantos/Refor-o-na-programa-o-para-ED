n1 = float(input("1° Nota: "))
n2 = float(input("2° Nota: "))
n3 = float(input("3° Nota: "))
media = (n1+ n2 +n3) / 3
print("A média foi de {:.1f}.".format(media))

if (media >= 7 and media != 10):
    print("Aluno  Aprovado!")
elif (media < 7) :
    print("Aluno Reprovado!")
elif (media == 10):
    print("Aluno Aprovado com Distinção!")

