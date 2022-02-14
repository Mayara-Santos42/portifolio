soma = 0
cont: int = 0
for c in range(0 , 6):
    number = int(input("Digite um número inteiro: "))
    if number % 2 == 0:
        cont = cont + 1
        soma = soma + number
print("O total de números pares é {}, e a soma entre eles é igual {}.".format(cont ,soma))