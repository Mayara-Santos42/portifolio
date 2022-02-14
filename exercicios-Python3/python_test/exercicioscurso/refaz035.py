print("É possível formar um triângulo com quaisquer medidas? ")
medida1 = float(input("Primeira medida = "))
medida2 = float(input("Segunda medida = "))
medida3 = float(input("Terceira medida = "))
if ((medida2 + medida3) > medida1) and ((medida1 + medida3) > medida2) and ((medida1 + medida2) > medida3):
    print("É um triângulo!")
else:
    print("Não é um triângulo!")


