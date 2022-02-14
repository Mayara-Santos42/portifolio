precoNormal = float(input("Qual é o valor a ser pago? "))
print("""OPÇÕES DE PAGAMENTO!
 1 = À vista no Dinheiro ou Cheque: 10% de desconto;
 2 = À vista no Cartão: 5% de desconto;
 3 = Em até 2x NO CARTÃO: preço normal;
 4 = 3x OU MAiS no cartão: 20% juros. """)
condicoes = int(input("Como deseja pagar? "))
if condicoes == 1:
    desconto10 = (precoNormal * 10) / 100
    valorFinal1: float = precoNormal - desconto10
    print("Valor final do produto (com 10% de desconto) R$ {}.".format(valorFinal1))
elif condicoes == 2:
    desconto5 = (precoNormal * 5)/100
    valorFinal2 = precoNormal - desconto5
    print("Valor final do produto (com 5% de desconto) R$ {}.".format(valorFinal2))
elif condicoes ==3:
    vezes2 = precoNormal / 2
    print("Valor final do produto R$ {}, com parcelas de R$ {:.2f}.".format(precoNormal, vezes2))
else:
    juros20 = (precoNormal * 20)/100
    valorFinal3 = precoNormal + juros20
    vezesPagar = int(input("Em quantas vezes deseja pagar?"))
    vezes3 = valorFinal3 / vezesPagar
    print("Valor final do produto R$ {:.2f}, com parcelas de R$ {:.2f}.".format(valorFinal3, vezes3))

