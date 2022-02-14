import random
print("NOME DOS ALUNOS!")
al1 = input("NOME: ")
al2 = input("NOME: ")
al3 = input("NOME: ")
al4 = input("NOME: ")

lista = [al1, al2, al3, al4]

escolhido = random.choice(lista)

print("O aluno é {}.".format(escolhido))