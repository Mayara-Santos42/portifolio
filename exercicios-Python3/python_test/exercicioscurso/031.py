print("Valor da passagem!")
distancia = float(input("Distância percorrida em KM = "))
if distancia <= 200:
    valor = distancia * 0.50
    print("Valor a pagar R$ {}.".format(valor))
else:
    if distancia > 200:
     valor2 = distancia * 0.45
     print("Valor a pagar R$ {}.".format(valor2))
