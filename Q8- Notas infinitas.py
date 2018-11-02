notas = []
n=0
while n != -1:
    n= float(input("Digite uma nota: "))
    notas.append(n)

print("Quantidade de notas: {}" .format(len(notas)-1))
print("   ")
print("Notas digitadas: ")
for l in range(len(notas)-1):
    print(notas[l])

print("    ")
print("Lista das notas invertida: ")
i= len(notas)-2
while i >= 0:
    print(notas[i])
    i= i-1

print("   ")
soma= 0
a=1
while a <= (len(notas)-1):
    soma = soma + notas[a-1]
    a+=1
print("Soma das notas: {}".format(soma))

media= soma / (len(notas)-1)
print("A média das notas é de: {:.1f}" .format(media))

mediaAlta= 0
for r in range(len(notas)-1):
    if notas [r] > media:
        mediaAlta+=1
print("{} nota(s) estavam acima da média calculada." .format(mediaAlta))

notaBaixa= 0
for k in range(len(notas)-1):
    if notas [r] < 7:
        notaBaixa+=1
print("{} nota(s) estavam abaixo de sete." .format(notaBaixa))

print("    ")
      
print("***Programa Encerrado***")
