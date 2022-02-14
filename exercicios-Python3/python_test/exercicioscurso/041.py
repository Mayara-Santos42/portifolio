print("CONFEDERAÇÃO NACIONAL DE NATAÇÃO! \nReferente a idade de nossos atletas.")
nascimento = int(input("Qual é o seu ano de nascimento? "))
idade = 2020 - nascimento
if idade <= 9:
    print("Sua idade é {}.\nAté 9 anos: MIRIM!".format(idade))
elif (idade >= 10) and (idade <= 14):
    print("Sua idade é {}.\nAté 14 anos: INFANTIL!".format(idade))
elif (idade >= 15) and (idade <= 19):
    print("Sua idade é {}.\nAté 19 anos: JUNIOR!".format(idade))
elif (idade == 20):
    print("Sua idade é {}.\nAté 20 anos: SÊNIOR!".format(idade))
else:
    print("Sua idade é {}.\nAcima: MASTER!".format(idade))