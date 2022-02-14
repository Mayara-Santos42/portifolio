print("AUMENTO SALARIAL!")
salarioInicial = float(input("Salário Atual = "))
if salarioInicial > 1250.00:
    aumento1 = salarioInicial * 10 / 100
    novoSalario1 = aumento1 + salarioInicial
    print("Aumento de R$ {}.\nNovo Salário R$ {}.".format(aumento1, novoSalario1))
else:
    if salarioInicial <= 1250.00:
        aumento2 = (salarioInicial * 15) / 100
        novoSalario2 = aumento2 + salarioInicial
        print("Aumento de R$ {}.\nNovo Salário R$ {}.".format(aumento2, novoSalario2))