from random import randint
comp = randint(0, 10)
print("ADIVINHE UM NÚMERO QUE O COMPUTADOR PENSOU ENTRE 0 & 10!")
print("Adivinhe!")
acer = False
palpite = 0
while not acer:
    jog = int(input("Palpite: "))
    palpite += 1
    if jog == comp:
        acer = True
    else:
        if jog < comp:
            print("Mais... Tente novamente!")
        elif jog > comp:
            print("Menos... Tente novamente!")
print("Acertou com {} palpites. Parabéns!".format(palpite))