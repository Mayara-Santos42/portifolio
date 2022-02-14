print("Qual o menor valor!?")
numero1 = float(input("Digite o primeiro número = "))
numero2 = float(input("Digite o segundo número = "))
numero3 = float(input("Digite o terceiro número = "))
if numero1 < numero2:
    print("O menor é: {}.".format(numero1))
else:
    if numero2 < numero3:
        print("O menor é: {}.".format(numero2))
    else:
        if numero3 > numero1:
            print("O menor é: {}.".format(numero3))
        else:
            if numero3 < numero2:
                print("O menor é: {}.".format(numero3))
