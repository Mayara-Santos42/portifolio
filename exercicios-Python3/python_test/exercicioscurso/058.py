import random
print("ADIVINHE O NÚMERO QUE O COMPUTADOR PENSOU!")
numero1 = random.randint(0 , 3)
numero2 = 1
numero2 = int(input("Digite um número inteiro entre 0 e 3 = "))
while numero2 != numero1:
    numero2 = int(input("Você errou! Digite novamente um número inteiro entre 0 e 3 = "))
    numero2 += 0
print("A máquina pensou em {}, e você deu {} palpites errados.".format(numero1, numero2))