somaIdade = 0
mediaIdade = 0
maiorIdadehomem = 0
nomeVelho = ""
totalMulher20 = 0
for pessoa in range(1, 5):
    print("---------- {}° PESSOA ------------".format(pessoa))
    nome = str(input("Qual é o seu nome? ")).strip()
    idade = int(input("A sua idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaIdade += idade
    if pessoa == 1 and sexo in "Mm":
        maiorIdadehomem = idade
        nomeVelho = nome
    if sexo in "Mn" and idade > maiorIdadehomem:
        maiorIdadehomem = idade
        nomeVelho = nome
    if sexo in "Ff" and idade < 20:
        totalMulher20 += 1
mediaIdade = somaIdade / 4
print("A média de idade do grupo é de {} anos.".format(mediaIdade))
print("O nome do homem mais velho é {}, possuindo {} anos.".format(nomeVelho, maiorIdadehomem))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totalMulher20))