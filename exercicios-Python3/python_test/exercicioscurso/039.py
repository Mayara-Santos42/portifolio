print("ALISTAMENTO MILITAR!")
anoPesquisa = int(input("Informe o ano sugerido para sua pesquisa: "))
anoNascimento = int(input("Qual é o ano do seu nascimento? "))
idade = anoPesquisa - anoNascimento
if idade < 18:
    faltam = 18 - idade
    print("Você ainda vai se alistar em {} ano(s).".format(faltam))
elif idade == 18:
    print("Você já deve fazer o alistamento! NÃO SE ESQUEÇA!")
else:
    idade > 18
    faltam = idade - 18
    print("Seu tempo de fazer o alistamento já passou em {} ano(s).".format(faltam))