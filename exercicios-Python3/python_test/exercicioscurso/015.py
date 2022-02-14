km = float(input("Quilomêtros percorridos: "))
dias = int(input("Quantidade de dias alugado: "))
pdia = dias * 60
rodado = km * 0.15
total = pdia + rodado

print("Valor a ser pago no final = {} ".format(total))