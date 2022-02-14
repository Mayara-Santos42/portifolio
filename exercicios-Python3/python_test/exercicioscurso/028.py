import random
print("ADIVINHE O NÚMERO QUE O COMPUTADOR PENSOU!")
numero1 = random.randint(0 , 5)
numero2 = int(input("Digite um número inteiro entre 0 e 5 = "))
if numero1 == numero2:
    print("Você ganhou!")
else:
    print("Número que a máquina pensou {}.".format(numero1))
    print("Infelizmente você perdeu!")

