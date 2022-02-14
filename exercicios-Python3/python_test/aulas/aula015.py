"""" cont = 1
while cont <= 10:
    print(cont, "-->", end=" ")
    cont += 1
print("Acabou") """

""" n = cont = 0
while cont < 3:
    n = int(input("Digite um número"))
    cont += 1 """

""" n = 0
while n != 999:
    n = int(input("Digite um número: ")) """

"""n = s = 0
while n!= 999:
    n = int(input("Digite um número: "))
    s += n
print("A soma vale {}.".format(s))"""

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
# print("A soma vale {}.".format(s))
# f = simplifica a string
print(f"A soma vale {s}")

nome = "José"
idade = 33
print(f"O {nome} tem {idade} anos.")