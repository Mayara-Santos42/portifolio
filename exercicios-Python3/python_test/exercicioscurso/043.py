print("""     TABELA DE IMC.
  MENOS DE 18.5: ABAIXO DO PESO!
  ENTRE 18.5 E 25: PESO IDEAL!
  ENTRE 25.1 E 30: SOBREPESO!
  ENTRE 30.1 E 40: OBESIDADE!
  ACIMA DE 40: OBESIDADE MÓRBIDA!""")
peso = float(input("Qual é o seu peso?" ))
altura = float(input("Qual a sua altura?" ))
imc = peso / (altura * altura)
print("Seu calcúlo de IMC é {:.1f}!".format(imc))
if imc < 18.5:
    print("VOCÊ SE ENCONTRA ABAIXO DO PESO!")
elif (imc >= 18.5) and (imc <= 25):
    print("Você se encontra no PESO IDEAL!")
elif (imc > 25) and (imc <= 30):
    print("Você se encontra SOBREPESO!")
elif (imc > 30) and (imc <= 40):
    print("VOCÊ SE ENCONTRA COM OBESIDADE!")
else:
    print("OBESIDADE MÓRBIDA! PROCURE UM ESPECIALISTA!")