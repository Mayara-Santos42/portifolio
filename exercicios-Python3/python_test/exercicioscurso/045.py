import random
print("JO-KEN-PÔ")
print("""ESCOLHA UMA DAS OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA""")
escolhaMesa = random.randint(1 , 3)
escolha = int(input("Faça sua escolha para jogar contra o computador: "))
if escolha == 1: # Você jogou PEDRA!
    if escolhaMesa == 1:
        print("Tente novamente!")
    elif escolhaMesa == 2:
        print("Você perdeu. Computador = {} ; Você = {}.".format(escolhaMesa, escolha))
    elif escolhaMesa == 3:
        print("Você ganhou. Computador = {} ; Você = {}.".format(escolhaMesa, escolha))
    else:
        print("Escolha inválida!")
elif escolha == 2: # Você jogou PAPEL!
    if escolhaMesa == 1:
        print("Você ganhou. Computador = {} ; Você = {}.".format(escolhaMesa, escolha))
    if escolhaMesa == 2:
        print("Tente novamente!")
    if escolhaMesa == 3:
        print("Você perdeu. Computador = {} ; Você = {}.".format(escolhaMesa, escolha))
    else:
        print("Escolha inválida!")
elif escolha == 3:
    if escolhaMesa == 1:
        print("Você perdeu. Computador = {} ; Você = {}.".format(escolhaMesa, escolha))
    if escolhaMesa == 2:
        print("Você ganhou. Computador = {} ; Você = {}.".format(escolhaMesa, escolha))
    if escolhaMesa == 3:
        print("Tente novamente!")
    else:
        print("Escolha inválida!")
else:
    print("Opção Inválida!")
