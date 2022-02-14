anoAtual = int(input("Qual é o ano atual? "))
totalMaior = 0
totalMenor = 0
for c in range(0 , 7):
    anoNascimento = int(input("Digite seu ano de nascimento: "))
    maioridade = anoAtual - anoNascimento
    if (maioridade >= 21):
        totalMaior += 1
    else:
        totalMenor += 1
print("")
print("Ao todo tivemos {} pessoas maiores de idade.".format(totalMaior))
print("E também tivemos {} pessoas menores de idade.".format(totalMenor))