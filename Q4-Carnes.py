
print("---- Tabela de carnes ----")
print("""File Duplo = [1]
Alcatra = [2]
Picanha = [3]""")

print("    ")

print("---- Tipo de pagamentos ----")
print("""Á vista = [1]
Cartão de crédito = [2]
Cartão Tabajara = [3] (5% de Desconto)""")

print("   ")

tipo= int(input("Tipo da carne: "))
quantidade = float(input("Quantidade de carne:[kg] "))
valor = 0

print("   ")

if tipo == 1:
      print("{}Kg de File Duplo".format(quantidade))
      if quantidade <= 5:
            valor= 4.9 * quantidade
      if quantidade > 5:
            valor = 5.8 * quantidade
elif tipo == 2:
      print("{}Kg de Alcantra".format(quantidade))
      if quantidade <= 5:
            valor= 5.9 * quantidade
      if quantidade > 5:
            valor = 6.8 * quantidade
elif tipo == 3:
      print("{}Kg de Picanha".format(quantidade))
      if quantidade <= 5:
            valor= 6.9 * quantidade
      if quantidade > 5:
            valor = 7.8 * quantidade

print ("Preço total: R${:.2f}".format(valor))
pagamento = int(input("Tipo de pagamento: "))

if  pagamento == 3:
      desconto= (valor -(valor * 5/100))
      print("5% de Desconto")
      print("Valor a pagar: R${:.2f}".format(desconto))

print("     ")
print("Obrigado(a), volte sempre!")
