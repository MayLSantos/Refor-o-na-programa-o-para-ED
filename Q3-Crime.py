soma= 0
print("Reponda 'sim' ou 'não'")
telefone = str(input("Telefonou para a vitima? "))
if telefone == 'sim':
    soma +=1
trabalho = str(input("Já trabalhou com a vitima? "))
if trabalho == 'sim':
    soma +=1
local = str(input("Esteve no local do crime? "))
if local == 'sim':
    soma +=1
moradia = str(input("Mora perto da vitima? "))
if moradia == 'sim':
    soma +=1
devia = str(input("Devia para a vitima? "))
if devia == 'sim':
    soma +=1

print("    ")

if soma == 2:
    print ("Suspeito")
elif soma == 3 or soma == 4:
    print ("Cúmplice")
elif soma == 5:
    print("Assassino")
else:
    print ("Inocente")
