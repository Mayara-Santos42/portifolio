import random
print("APRESENTAÇÃO DO TRABALHO:")
al1 = input("ALUNO = ")
al2 = input("ALUNO = ")
al3 = input("ALUNO = ")
al4 = input("ALUNO = ")

lista = [al1 , al2, al3, al4]
random.shuffle(lista)

print("Ordem: {}".format(lista))