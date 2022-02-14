"""Dados N e N sequências de números interios não-nulos,
cada qual seguida por um 0.
Calcule a soma dos números pares dessa sequência."""

sequencia = int(input("Digite o número de sequências: "))
print("")
for i in range(sequencia):
    print("Sequência de {}".format(sequencia))
    numero = int(input("Digite um número da sequência: "))
    soma = 0 #Para cada sequência
    while numero != 0 :
        if numero % 2 == 0:
            soma = soma + numero
        numero = int(input("Digite um número da sequência: "))

    print("A soma da sequencia {} é {}.".format(i+1, soma))
    print("")
