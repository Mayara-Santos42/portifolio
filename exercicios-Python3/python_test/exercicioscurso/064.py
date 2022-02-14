totalS = totalT = soma = 0
termos = 1
n = soma
n = int(input("Digite um número inteiro [999 para parar]: "))
while n != 999:
    totalT = totalT + termos
    soma += n
    totalS = soma + 0
    n = int(input("Digite um número inteiro [999 para parar]: "))
print("A quantidade de termos digitados foram {}.".format(totalT))
print("E a soma entre todos os números é de {}.".format(totalS))
