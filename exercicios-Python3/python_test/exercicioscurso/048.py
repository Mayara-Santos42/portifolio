soma = 0
conta = 0
for numeros in range(1 , 500):
    if (numeros / 3) % 2 == 1:
        conta = conta + 1
        soma = soma + numeros
print("A soma de todos os {} números, é {}.".format(conta ,soma))