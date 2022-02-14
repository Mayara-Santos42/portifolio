velocidade = float(input("Digite qual foi a velocidade que você fez esse trajeto = "))
multa = (velocidade - 80.00) * 7.00
if velocidade > 80.00:
    print("Você foi multado!! Valor R$ {:.2f}.".format(multa))
else:
   print("Parabéns! Você andou no limite.")
