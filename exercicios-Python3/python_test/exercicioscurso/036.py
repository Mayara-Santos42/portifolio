# EMPRÉSTIMO BÁNCARIO PARA COMPRAR UMA CASA (financiamento)!!//
valordaCasa = float(input("Qual é o valor da casa que deseja comprar? "))
salarioComprador = float(input("Qual é o seu sálario? "))
anosPagamento = int(input("E por fim em quantos anos deseja pagar? "))
prestacaoMensal = valordaCasa / (anosPagamento * 12)
if  prestacaoMensal < ((salarioComprador * 30) / 100) :
    print("FINANCIAMENTO APROVADO!")
else:
    print("INFELIMENTE SEU FINCANCIAMENTO FOI NEGADO!")