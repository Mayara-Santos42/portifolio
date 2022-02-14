totalS = soma = totalT = maior = menor = 0
n = soma = 0
termos = 1
p = ''
while p != "N":
    n = int(input("Digite um número inteiro: "))
    totalS += soma + n
    totalT = totalT + termos
    media = totalS / totalT
    if totalT == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = str(input("Deseja continuar? [S/N]? ")).upper()
print("A soma entre os números é de {}.".format(totalS), end=' ')
# print("E a quantidade de termos foram {}.".format(totalT))
print("E a média entre eles é {:.2f}.".format(media))
print("Por fim, o maior valor foi {} e o menor foi {}.".format(maior, menor))