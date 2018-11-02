nomesCarros= ['Fusca','Gol','Uno', 'Vectra', 'Peugeot 308']
kmLitro= [7, 10, 12.5, 9, 14.5]

economico= 1
for i in range(len(kmLitro)):
    economico= kmLitro [i]


for a in range(len(kmLitro)):
    if kmLitro[a] == economico:
        print("O carro de menor consumo é o {}" .format(nomesCarros[a]))

r= 0
for r in range(len(kmLitro)):
    combustivel= 1000 / kmLitro[r]
    dinheiro=3.5 * combustivel
    print("{}- {} - {:.1f} litros por km - {:.1f} litros ao pecorrer 1000 km- R${:.2f}.".format(r+1,nomesCarros[r], kmLitro[r], combustivel, dinheiro))
    print("   ")
