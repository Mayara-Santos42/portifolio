print("Média Final Escolar!")
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
mediaFinal = (nota1 + nota2) / 2
if mediaFinal < 5.0:
    print("Você foi REPROVADO! \nPois sua média foi = {}.!".format(mediaFinal))
elif (mediaFinal >= 5.0) and (mediaFinal <= 6.9):
    print("Você está em RECUPERAÇÃO! \nPois sua média foi = {}!".format(mediaFinal))
else:
    print("Você foi APROVADO! \nCom média = {}! \nParabéns!".format(mediaFinal))