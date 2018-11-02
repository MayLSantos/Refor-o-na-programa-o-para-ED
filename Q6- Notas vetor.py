notas = []
for i in range(4):
    n= float(input("Nota {}: " .format(i+1)))
    notas.append(n)

print("    ")
print("BOLETIM")

for i in range(4):
    print("{} Nota: {}" .format(i+1,notas[i]))

media= (notas[0] + notas [1] + notas [2] + notas[3])/4
print("Média do aluno: {}" .format (media))            
