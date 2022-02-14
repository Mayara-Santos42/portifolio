ano = int(input("DIGITE UM ANO QUALQUER: "))
bissexto = ano % 4
if bissexto == 0:
    print("É um ano bissexto!")
else:
    print("Não é um ano bissexto!")